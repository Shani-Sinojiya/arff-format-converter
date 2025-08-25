"""Utility functions for ARFF Format Converter."""

import time
from pathlib import Path
from typing import Optional

from .exceptions import ValidationError, FileFormatError


def validate_file_path(file_path: Path) -> None:
    """
    Validate that the input file exists and is a valid ARFF file.

    Args:
        file_path: Path to the file to validate

    Raises:
        ValidationError: If file doesn't exist or is not accessible
        FileFormatError: If file is not an ARFF file
    """
    if not file_path.exists():
        raise ValidationError(f"File does not exist: {file_path}")

    if not file_path.is_file():
        raise ValidationError(f"Path is not a file: {file_path}")

    if not file_path.suffix.lower() == '.arff':
        raise FileFormatError(f"File is not an ARFF file: {file_path}")

    try:
        # Test if file is readable
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if not first_line.lower().startswith('@relation'):
                raise FileFormatError(f"Invalid ARFF file format: {file_path}")
    except UnicodeDecodeError:
        # Try with different encoding
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                first_line = f.readline().strip()
                if not first_line.lower().startswith('@relation'):
                    raise FileFormatError(
                        f"Invalid ARFF file format: {file_path}")
        except Exception as e:
            raise ValidationError(f"Cannot read file: {file_path}. Error: {e}")
    except Exception as e:
        raise ValidationError(f"Cannot access file: {file_path}. Error: {e}")


def validate_output_format(output_format: str) -> None:
    """
    Validate the output format.

    Args:
        output_format: The output format to validate

    Raises:
        ValidationError: If format is not supported
    """
    supported_formats = {"csv", "json", "xml", "xlsx", "parquet", "orc"}

    if output_format.lower() not in supported_formats:
        raise ValidationError(
            f"Unsupported output format: {output_format}. "
            f"Supported formats: {', '.join(sorted(supported_formats))}"
        )


def create_output_path(
    input_file: Path,
    output_dir: Path,
    output_format: str,
    custom_filename: Optional[str] = None,
) -> Path:
    """
    Create the output file path.

    Args:
        input_file: Input file path
        output_dir: Output directory
        output_format: Output format extension
        custom_filename: Custom filename (optional)

    Returns:
        Complete output file path
    """
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    if custom_filename:
        # Use custom filename
        base_name = Path(custom_filename).stem
    else:
        # Use input filename with timestamp for uniqueness
        base_name = f"{input_file.stem}_{int(time.time())}"

    output_filename = f"{base_name}.{output_format}"
    return output_dir / output_filename


def get_file_size_mb(file_path: Path) -> float:
    """
    Get file size in megabytes.

    Args:
        file_path: Path to the file

    Returns:
        File size in MB
    """
    return file_path.stat().st_size / (1024 * 1024)


def format_duration(seconds: float) -> str:
    """
    Format duration in a human-readable way.

    Args:
        seconds: Duration in seconds

    Returns:
        Formatted duration string
    """
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.2f}s"
    else:
        minutes = int(seconds // 60)
        remaining_seconds = seconds % 60
        return f"{minutes}m {remaining_seconds:.1f}s"


def estimate_memory_usage(num_rows: int, num_cols: int) -> float:
    """
    Estimate memory usage for a DataFrame.

    Args:
        num_rows: Number of rows
        num_cols: Number of columns

    Returns:
        Estimated memory usage in MB
    """
    # Rough estimation: 8 bytes per numeric value, 50 bytes average per string
    avg_bytes_per_cell = 25  # Conservative estimate
    total_bytes = num_rows * num_cols * avg_bytes_per_cell
    return total_bytes / (1024 * 1024)


def get_optimal_chunk_size(file_size_mb: float, available_memory_mb: float = 1024) -> int:
    """
    Calculate optimal chunk size based on file size and available memory.

    Args:
        file_size_mb: File size in megabytes
        available_memory_mb: Available memory in megabytes

    Returns:
        Optimal chunk size (number of rows)
    """
    # Conservative approach: use 25% of available memory
    target_memory_mb = available_memory_mb * 0.25

    if file_size_mb <= target_memory_mb:
        # File is small enough to process entirely
        return 100000  # Large chunk size

    # Calculate chunk size to fit in target memory
    ratio = target_memory_mb / file_size_mb
    base_chunk_size = 10000

    return max(1000, int(base_chunk_size * ratio))


# Legacy function for backward compatibility
def process(filename: str, output_folder: str, output_format: str, fast: bool = False):
    """Legacy process function for backward compatibility."""
    import os
    from pathlib import Path
    from .validate import validate_file_path, validate_output_folder, validate_output_format
    from .output import build_output
    from scipy.io import arff
    import pandas as pd
    import time

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

    build_output(df, output_folder, output_path, output_format, fast)

    # Greet and show path
    print(f"File converted successfully to {output_format.upper()} format.")
    print(f"Output file: {output_path}")
    print("")
    print("Thank you for using ARFF Format Converter.")
    print("Please consider leaving a star on the GitHub repository.")
    print("https://github.com/Shani-Sinojiya/arff-format-converter")
    print("")
    print("Have a great day!")
    print("")


def main():
    """Legacy main function - use CLI instead."""
    import argparse
    from .texts import bottom_msg
    from .__init__ import __version__

    parser = argparse.ArgumentParser(
        description="Convert ARFF files to different formats.",
        epilog=bottom_msg,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--file", "-f", help="Path to the ARFF file.", type=str, required=True)
    parser.add_argument(
        "--output", "-o", help="Path to the output folder.", type=str, required=True)
    parser.add_argument(
        "--format", "-fmt", help="Output format: 'xml', 'json', 'csv', 'xlsx', 'orc', 'parquet'.",
        choices=["xml", "json", "csv", "xlsx", "orc", "parquet"],
        type=str, required=True)
    parser.add_argument(
        "--fast", action="store_true", help="Enable fast mode for faster conversion.")
    parser.add_argument(
        "--version", "-v", action="version", version=__version__)

    args = parser.parse_args()

    process(args.file, args.output, args.format, args.fast)
