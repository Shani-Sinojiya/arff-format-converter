import ujson as json
import csv
import fastavro
import pandas as pd
from .validate import *
from tqdm import tqdm


try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


# XML Encodeing Start
def build_nodes(data, name, parent):
    if isinstance(data, list):
        for item in data:
            build_nodes(item, name, ET.SubElement(parent, name))
    elif isinstance(data, dict):
        for attr in data:
            build_nodes(data[attr], name=attr, parent=parent)
    else:
        parent.text = data


def output_xml(schema, outfile):
    progress_bar = tqdm(total=100, desc='Writing XML', unit=" %",
                        position=5, leave=False, colour="red")
    progress_bar.update(25 - progress_bar.n)
    root = ET.Element('dataset')
    progress_bar.update(50 - progress_bar.n)
    build_nodes(schema, 'dataset', root)
    progress_bar.update(70 - progress_bar.n)
    ET.ElementTree(root).write(outfile, encoding="utf-8", xml_declaration=True)
    progress_bar.update(100 - progress_bar.n)
# XML Encoding End


# JSON Encoding Start
def output_json(schema, outfile):
    for line in tqdm(json.dumps(schema, ensure_ascii=False, escape_forward_slashes=False),
                     desc="Writing JSON", unit=" words", leave=False, colour="red"):
        outfile.write(line)
# JSON Encoding End


# CSV Encoding Start
def output_csv(schema, outfile):
    progress_bar = tqdm(total=100, desc='Writing CSV', unit=" %",
                        position=5, leave=False, colour="red")
    progress_bar.update(10 - progress_bar.n)
    csv_writer = csv.DictWriter(
        outfile, fieldnames=[attr["name"] for attr in schema["attributes"]])
    progress_bar.update(25 - progress_bar.n)
    csv_writer.writeheader()
    progress_bar.update(50 - progress_bar.n)
    csv_writer.writerows(schema["data"])
    progress_bar.update(100 - progress_bar.n)
# CSV Encoding End


# Excel Encoding Start
def output_excel(schema, outfile):
    chunk_size = 1_000_000  # Set the chunk size as needed
    engine = "openpyxl"

    df = pd.DataFrame(schema["data"])

    # Calculate the number of chunks
    num_chunks = (len(df) // chunk_size) + 1

    with pd.ExcelWriter(outfile, engine=engine) as writer:
        for i in tqdm(range(num_chunks), desc="Writing Excel Sheets", unit=" sheet", dynamic_ncols=True, leave=True, colour="green"):
            start_idx = i * chunk_size
            end_idx = (i + 1) * chunk_size
            chunk_df = df.iloc[start_idx:end_idx, :]

            sheet_name = f'Sheet_{i}'
            chunk_df.to_excel(writer, sheet_name=sheet_name,
                              index=False, engine=engine, header=True)
# Excel Encoding End


# OCR Encoding Start
def output_orc(schema, outfile):
    progress_bar = tqdm(total=100, desc='Writing ORC', unit=" %",
                        position=20, leave=False, colour="red")
    try:
        table = pd.DataFrame(schema["data"])

        avro_schema = {
            "type": "record",
            "name": "RecordName",
            "fields": [
                {"name": col, "type": ["null", "string"]} for col in table.columns
            ]
        }

        with open(outfile, 'wb') as orc_file:
            fastavro.writer(orc_file, schema=avro_schema,
                            records=table.to_dict(orient='records'))
    except ImportError:
        log_error(
            0, OTHER_ERROR, "Fastavro library not installed. Please install it using 'pip install fastavro'.")
    progress_bar.update(100 - progress_bar.n)
# OCR Encoding End


OUTPUT_FORMAT_FUNCTIONS = {
    'json': output_json,
    'csv': output_csv,
    'xlsx': output_excel,
    'orc': output_orc,
    'xml': output_xml
}


def build_output(schema, outfile, output_format: str):
    if output_format in OUTPUT_FORMAT_FUNCTIONS:
        try:
            OUTPUT_FORMAT_FUNCTIONS[output_format](
                schema, outfile)
        except Exception as e:
            log_error(0, OTHER_ERROR, "Error Occured. Please try Again")
            exit_with_errors()
    else:
        log_error(0, OPTION_ERROR,
                  "Invalid output format. Please provide a valid output format.")
        exit_with_errors()
