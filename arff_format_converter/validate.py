"""Legacy validation functions for backward compatibility."""

import os
import sys
from pathlib import Path

from .config import legal_formats
from .exceptions import ValidationError, FileFormatError


# Legacy error codes
FILE_ERROR = 0
OPTION_ERROR = 1
OTHER_ERROR = 2

error_array = [
    "Invalid file extension - expects '<filename>.arff'",
    "Invalid option - expects 'xml', 'json', 'csv', 'xlsx', 'orc' or 'parquet'.",
    "The file format is invalid."
]

error_log = []


def console(msg: object):
    """Legacy console function."""
    print(msg, file=sys.stderr)


def log_error(line_num, error_index, details):
    """Legacy error logging function."""
    this_error = {
        "line_num": line_num,
        "message": error_array[error_index],
        "details": details
    }
    error_log.append(this_error)
    console(f"Error at {line_num}:")
    console(error_array[error_index])
    console(details)


def exit_with_errors():
    """Legacy exit function."""
    console("Exiting with errors.")
    sys.exit(1)


def validate_file_path(path: str):
    """
    Legacy validation function for file path.

    Args:
        path: File path as string
    """
    if not os.path.isfile(path):
        log_error(
            0, FILE_ERROR,
            "Invalid file path. Please provide a valid path to the ARFF file."
        )
        exit_with_errors()

    # Check if it's an ARFF file
    if not path.lower().endswith('.arff'):
        log_error(
            0, FILE_ERROR,
            "Invalid file extension - expects '<filename>.arff'"
        )
        exit_with_errors()


def validate_output_folder(path: str):
    """
    Legacy validation function for output folder.

    Args:
        path: Output folder path as string
    """
    # Create directory if it doesn't exist
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        log_error(
            0, FILE_ERROR,
            f"Cannot create output folder: {e}"
        )
        exit_with_errors()


def validate_output_format(output_format: str):
    """
    Legacy validation function for output format.

    Args:
        output_format: Output format string
    """
    if output_format not in legal_formats:
        log_error(
            0, OPTION_ERROR,
            "Invalid output format. Please provide a valid output format."
        )
        exit_with_errors()
