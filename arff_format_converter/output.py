"""Legacy output functions for backward compatibility."""

import itertools
import sys
import threading
import time
from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.orc as orc

from .validate import exit_with_errors


def build_output(df: pd.DataFrame, output_folder: str, output_path: str, output_format: str, fast: bool = False):
    """
    Legacy function to convert DataFrame to various file formats.

    Args:
        df: Input DataFrame to convert
        output_folder: Output folder path (for compatibility)
        output_path: Full path to output file
        output_format: Desired output file format
        fast: Enable fast mode
    """
    done = False

    def animate():
        """Show spinning animation during conversion."""
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
            "xml": lambda: _convert_to_xml_legacy(df, output_path),
            "json": lambda: df.to_json(
                output_path,
                orient="records",
                indent=2,
                compression=("infer" if fast else None)
            ),
            "csv": lambda: df.to_csv(
                output_path,
                index=False,
                chunksize=(10000 if fast else None)
            ),
            "xlsx": lambda: df.to_excel(
                output_path,
                index=False,
                engine='openpyxl'
            ),
            "orc": lambda: orc.write_table(
                pa.Table.from_pandas(df, preserve_index=False),
                output_path,
                compression=("snappy" if fast else "zlib")
            ),
            "parquet": lambda: df.to_parquet(
                output_path,
                index=False,
                compression=("snappy" if fast else "gzip")
            )
        }

        if output_format in output_functions:
            output_functions[output_format]()
        else:
            print("Invalid output format. Please provide a valid output format.")
            exit_with_errors()

    except Exception as e:
        print(f"{output_format.upper()} conversion error: {e}")
        exit_with_errors()
    finally:
        stop_animation()
        sys.stdout.write('\r' + ' ' * 20 + '\r')  # Clear the animation
        sys.stdout.flush()


def _convert_to_xml_legacy(df: pd.DataFrame, output_path: str) -> None:
    """Legacy XML conversion function."""
    try:
        # Use pandas to_xml if available (pandas >= 1.3.0)
        df.to_xml(output_path, index=False, parser="etree")
    except AttributeError:
        # Fallback for older pandas versions
        xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
        xml_content.append('<data>')

        for _, row in df.iterrows():
            xml_content.append('  <record>')
            for col, value in row.items():
                # Escape XML special characters
                escaped_value = str(value).replace('&', '&amp;').replace(
                    '<', '&lt;').replace('>', '&gt;')
                xml_content.append(f'    <{col}>{escaped_value}</{col}>')
            xml_content.append('  </record>')

        xml_content.append('</data>')

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(xml_content))
