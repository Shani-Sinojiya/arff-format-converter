import os
import argparse
from .validate import *
from .texts import *
from .output import *

import time

from scipy.io import arff
import pandas as pd


def process(filename: str, output_folder: str, output_format: str):
    validate_file_path(filename)
    validate_output_folder(output_folder)
    validate_output_format(output_format)

    data, _ = arff.loadarff(filename)

    df = pd.DataFrame(data)

    for column in df.columns:
        if df[column].dtype == object:
            df[column] = df[column].apply(lambda x: x.decode(
                'utf-8') if isinstance(x, bytes) else x)

    output_path = os.path.join(output_folder, f"{os.path.splitext(
        os.path.basename(filename))[0]}_{int(time.time())}.{output_format}")

    build_output(df, output_folder, output_path)

    # Greet and show path
    print(f"File converted successfully to {output_format.upper()} format.")
    print(f"Output file: {output_path}")
    print("")
    print("Thank you for using ARFF Format Converter.")
    print("")


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
