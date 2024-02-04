from .logs import *
import os


def validate_file_path(path: str):
    if not os.path.isfile(path):
        log_error(
            0, FILE_ERROR, "Invalid file path. Please provide a valid path to the ARFF file.")
        exit_with_errors()


def validate_output_folder(path: str):
    if not os.path.isdir(path):
        log_error(
            0, FILE_ERROR, "Invalid output folder path. Please provide a valid path to the output folder.")
        exit_with_errors()


def validate_output_format(output_format: str):
    if output_format not in legal_formats:
        log_error(0, OPTION_ERROR,
                  "Invalid output format. Please provide a valid output format.")
        exit_with_errors()
