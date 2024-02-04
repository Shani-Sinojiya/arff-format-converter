import os
import argparse
from tqdm import tqdm
from .validate import *
from .texts import *
from .output import *


def process(filename: str, output_folder: str, output_format: str):
    validate_file_path(filename)
    validate_output_folder(output_folder)
    validate_output_format(output_format)

    readdata = False
    output_path = os.path.join(output_folder, f"{os.path.splitext(
        os.path.basename(filename))[0]}.{output_format}")

    with open(filename, 'r') as infile:
        schema = {"relation": "", "attributes": [], "data": []}

        for line in infile:
            if line[0] == "%":
                continue
            elif line[0] == "@":
                args = line.split()
                if args[0] == "@relation":
                    schema["relation"] = args[1]
                elif args[0] == "@attribute":
                    values = "".join(args[2:])
                    if values[0] == "{":
                        values = values[1:len(values)-1]
                        values = values.split(",")
                    schema["attributes"].append(
                        {"name": args[1], "values": values})
                elif args[0] == "@data":
                    readdata = True
            elif readdata:
                schema["data"].append(line.strip())

        names = []
        data = []
        attrs = schema["attributes"]

        for attr in attrs:
            names.append(attr["name"])

        for row in tqdm(schema["data"], desc="Reading From File", unit="row", dynamic_ncols=True, leave=False, colour="blue"):
            row = row.split(",")
            entry = {}
            for name in names:
                entry[name] = row[names.index(name)]
            data.append(entry)

        schema["data"] = data

        if output_format == "xml" or output_format == "xlsx" or output_format == "orc":
            build_output(schema, output_path, output_format)
        else:
            with open(output_path, 'w') as outfile:
                build_output(schema, outfile, output_format)

    print(f"\nFile converted into {output_format} format.")
    print(f"Output saved to: {os.path.abspath(output_path)}")
    print("Thanks for using arff-format-converter")


def main():
    parser = argparse.ArgumentParser(
        description="Convert ARFF files to different formats.",
        epilog=bottom_msg,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--file", "-f", help="Path to the ARFF file.", type=str, required=True)
    parser.add_argument(
        "--output", "-o", help="Path to the output folder.", type=str, required=True)
    parser.add_argument(
        "--format", "-fmt", help="Output format: 'xml', 'json', 'csv', 'xlsx', 'orc'.",
        choices=["xml", "json", "csv", "xlsx", "orc"],
        type=str, required=True)

    args = parser.parse_args()

    process(args.file, args.output, args.format)
