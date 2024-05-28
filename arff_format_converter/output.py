import pyarrow as pa
import pandas as pd
from .logs import exit_with_errors
import itertools
import threading
import time
import sys

import pyarrow.orc as orc


def build_output(df: pd.DataFrame, output_file: str, output_format: str):
    done = False

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\Converting ' + c)
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)

    match output_format:
        case "xml":
            t.start()
            try:
                df.to_xml(output_file, parser="etree", index=False)
            except Exception as e:
                print("XML: ", e)
                exit_with_errors()
            done = True
        case "json":
            t.start()
            try:
                df.to_json(output_file, orient="records", index=False)
            except Exception as e:
                print("JSON: ", e)
                exit_with_errors()
            done = True
        case "csv":
            t.start()
            try:
                df.to_csv(output_file, index=False)
            except Exception as e:
                print("CSV: ", e)
                exit_with_errors()
            done = True
        case "xlsx":
            t.start()
            try:
                df.to_excel(output_file, index=False)
            except Exception as e:
                print("Excel: ", e)
                exit_with_errors()
            done = True
        case "orc":
            t.start()
            try:
                table = pa.Table.from_pandas(df, preserve_index=False)
                orc.write_table(table, 'your_df.orc')
            except Exception as e:
                print("ORC: ", e)
                exit_with_errors()
            done = True

        case _:
            print("Invalid output format. Please provide a valid output format.")
            exit_with_errors()
