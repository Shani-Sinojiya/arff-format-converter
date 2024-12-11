import pyarrow as pa
import pandas as pd
from .logs import exit_with_errors
import itertools
import threading
import time
import sys

import pyarrow.orc as orc


def build_output(df: pd.DataFrame, output_file: str, output_format: str, fast: bool = False):
    """
    Converts a pandas DataFrame to various file formats and writes to the specified output file.

    Args:
        df (pd.DataFrame): The input DataFrame to convert.
        output_file (str): The path to the output file.
        output_format (str): The desired output file format (xml, json, csv, xlsx, orc, parquet).
    """
    done = False

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rConverting ' + c)
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()

    def stop_animation():
        nonlocal done
        done = True
        t.join()

    try:
        output_functions = {
            "xml": lambda: df.to_xml(output_file, parser="etree", index=False, compression=("infer" if fast else None)),
            "json": lambda: df.to_json(output_file, orient="records", index=False, compression=("infer" if fast else None)),
            "csv": lambda: df.to_csv(output_file, index=False, chunksize=(1000 if fast else None)),
            "xlsx": lambda: df.to_excel(output_file, index=False, chunksize=(1000 if fast else None)),
            "orc": lambda: orc.write_table(pa.Table.from_pandas(df, preserve_index=False), output_file, compression=("snappy" if fast else None)),
            "parquet": lambda: df.to_parquet(output_file, index=False, compression=("snappy" if fast else None))
        }

        if output_format in output_functions:
            output_functions[output_format]()
        else:
            print("Invalid output format. Please provide a valid output format.")
            exit_with_errors()
    except Exception as e:
        print(f"{output_format.upper()}: ", e)
        exit_with_errors()
    finally:
        stop_animation()
