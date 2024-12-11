import sys

FILE_ERROR = 0
OPTION_ERROR = 1
OTHER_ERROR = 2
legal_formats = ["xml", "json", "csv", "xlsx", "orc", "parquet"]
error_array = ["Invalid file extension - expects '<filename>.arff'",
               "Invalid option - expects 'xml', 'json', 'csv', 'xlsx', 'orc' or 'parquet'.", "The file format is invalid."]
error_log = []


def console(msg: object):
    print(msg, file=sys.stderr)


def log_error(line_num, error_index, details):
    this_error = {"line_num": line_num,
                  "message": error_array[error_index], "details": details}
    error_log.append(this_error)
    console(f"Error at {line_num}:")
    console(error_array[error_index])
    console(details)


def exit_with_errors():
    console("Exiting with errors.")
    sys.exit(1)
