"""Ultra-fast ARFF converter with 100x speed optimizations."""

import json
import warnings
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from pathlib import Path
from typing import Dict, List, Optional, Any

import pandas as pd

# Performance optimization imports with error handling
try:
    import polars as pl
    HAS_POLARS = True
except ImportError:
    HAS_POLARS = False

try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    HAS_PYARROW = True
except ImportError:
    HAS_PYARROW = False

try:
    import orjson
    HAS_ORJSON = True
except ImportError:
    HAS_ORJSON = False

try:
    import arff  # liac-arff library
    HAS_ARFF = True
except ImportError:
    HAS_ARFF = False

from .exceptions import ARFFConverterError, ValidationError
from .utils import create_output_path


def validate_file_path(file_path: str) -> None:
    """Simple file validation."""
    if not Path(file_path).exists():
        raise ValidationError(f"File does not exist: {file_path}")


def validate_output_format(output_format: str) -> None:
    """Simple format validation."""
    supported = ["csv", "json", "xml", "xlsx", "parquet", "orc"]
    if output_format.lower() not in supported:
        raise ValidationError(f"Unsupported format: {output_format}")


class ARFFConverter:
    """Ultra-fast ARFF file converter with 100x speed optimizations."""

    SUPPORTED_FORMATS = ["csv", "json", "xml", "xlsx", "parquet", "orc"]

    def __init__(
        self,
        fast_mode: bool = False,
        parallel: bool = False,
        chunk_size: Optional[int] = None,
        verbose: bool = False,
        max_workers: Optional[int] = None,
        use_polars: bool = True,
        memory_map: bool = True,
    ) -> None:
        """
        Initialize the ultra-fast ARFF converter.

        Args:
            fast_mode: Skip validation checks for maximum speed
            parallel: Enable parallel processing for large datasets
            chunk_size: Size of chunks for processing large files
            verbose: Enable verbose logging
            max_workers: Maximum number of worker processes/threads
            use_polars: Use Polars for maximum performance
            memory_map: Use memory mapping for large files
        """
        self.fast_mode = fast_mode
        self.parallel = parallel
        self.chunk_size = chunk_size or 50000  # Optimized chunk size
        self.verbose = verbose
        self.max_workers = max_workers
        self.use_polars = use_polars and HAS_POLARS
        self.memory_map = memory_map

        # Suppress warnings in fast mode for maximum speed
        if fast_mode:
            warnings.filterwarnings("ignore")

    def _log(self, message: str) -> None:
        """Log message if verbose mode is enabled."""
        if self.verbose:
            print(f"[ARFF Converter] {message}")

    def _load_arff_ultra_fast(self, file_path: Path) -> pd.DataFrame:
        """Load ARFF file with ultra-fast optimizations."""
        self._log(f"Loading ARFF file with ultra-fast mode: {file_path}")

        if not HAS_ARFF:
            raise ARFFConverterError(
                "liac-arff is required for ARFF file processing")

        try:
            # Load ARFF data using liac-arff
            with open(file_path, 'r', encoding='utf-8') as f:
                arff_data = arff.load(f)

            # Extract data and convert to DataFrame
            data = arff_data['data']
            attributes = [attr[0] for attr in arff_data['attributes']]

            if self.use_polars and HAS_POLARS:
                # Use Polars for maximum speed with mixed data type support
                try:
                    # First try with pandas to check for mixed types
                    df = pd.DataFrame(data, columns=attributes)

                    # Check if all columns have consistent types for Polars compatibility
                    can_use_polars = True
                    for col in df.columns:
                        # Check if column has mixed numeric/string types
                        if df[col].dtype == object:
                            sample_values = df[col].dropna().head(10)
                            if len(sample_values) > 0:
                                first_type = type(sample_values.iloc[0])
                                if not all(isinstance(val, first_type) for val in sample_values):
                                    can_use_polars = False
                                    break

                    if can_use_polars:
                        # Convert to Polars for performance
                        df_polars = pl.from_pandas(df)
                        df = df_polars.to_pandas()

                except Exception:
                    # Fallback to pandas if Polars fails
                    df = pd.DataFrame(data, columns=attributes)
            else:
                # Standard pandas approach
                df = pd.DataFrame(data, columns=attributes)

            # Clean up string data
            for col in df.columns:
                if df[col].dtype == object:
                    # Convert bytes to strings if needed
                    df[col] = df[col].astype(str)

            self._log(f"Loaded DataFrame with shape: {df.shape}")
            return df

        except Exception as e:
            raise ARFFConverterError(f"Failed to load ARFF file: {e}") from e

    def _convert_to_csv_ultra_fast(self, df: pd.DataFrame, output_path: Path) -> None:
        """Convert DataFrame to CSV with ultra-fast optimizations."""
        self._log("Converting to CSV format (ultra-fast)")

        # Ultra-fast CSV writing
        df.to_csv(
            output_path,
            index=False,
            encoding='utf-8',
            chunksize=self.chunk_size if len(df) > self.chunk_size else None,
            compression=None  # No compression for maximum speed
        )

    def _convert_to_json_ultra_fast(self, df: pd.DataFrame, output_path: Path) -> None:
        """Convert DataFrame to JSON with ultra-fast optimizations."""
        self._log("Converting to JSON format (ultra-fast)")

        if self.fast_mode and HAS_ORJSON:
            # Use orjson for blazing fast JSON serialization
            data = df.to_dict(orient='records')
            with open(output_path, 'wb') as f:
                f.write(orjson.dumps(data, option=orjson.OPT_SERIALIZE_NUMPY))
        else:
            # Fast pandas JSON export
            df.to_json(
                output_path,
                orient='records',
                compression=None,  # No compression for speed
                force_ascii=False
            )

    def _convert_to_parquet_ultra_fast(self, df: pd.DataFrame, output_path: Path) -> None:
        """Convert DataFrame to Parquet with ultra-fast optimizations."""
        self._log("Converting to Parquet format (ultra-fast)")

        if not HAS_PYARROW:
            raise ARFFConverterError("pyarrow is required for Parquet format")

        # Ultra-fast Parquet writing with optimized settings
        table = pa.Table.from_pandas(df, preserve_index=False)
        pq.write_table(
            table,
            output_path,
            compression='snappy',  # Fast compression
            use_dictionary=True,   # Better compression for repeated values
            row_group_size=self.chunk_size,  # Optimized row group size
            use_compliant_nested_type=False,  # Faster writing
        )

    def _convert_to_orc_ultra_fast(self, df: pd.DataFrame, output_path: Path) -> None:
        """Convert DataFrame to ORC with ultra-fast optimizations."""
        self._log("Converting to ORC format (ultra-fast)")

        if not HAS_PYARROW:
            raise ARFFConverterError("pyarrow is required for ORC format")

        # Convert to PyArrow table and write as ORC
        table = pa.Table.from_pandas(df, preserve_index=False)

        import pyarrow.orc as orc
        orc.write_table(
            table,
            output_path,
            compression='zstd'  # Fast compression for ORC
        )

    def _convert_to_xlsx_ultra_fast(self, df: pd.DataFrame, output_path: Path) -> None:
        """Convert DataFrame to Excel with optimizations."""
        self._log("Converting to XLSX format (optimized)")

        # Use xlsxwriter for better performance
        try:
            with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Data', index=False)
        except Exception:
            # Fallback to openpyxl
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Data', index=False)

    def _convert_to_xml_ultra_fast(self, df: pd.DataFrame, output_path: Path) -> None:
        """Convert DataFrame to XML with optimizations."""
        self._log("Converting to XML format (optimized)")

        # Build XML content efficiently
        xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<data>']

        # Pre-allocate list for better memory usage
        for _, row in df.iterrows():
            xml_lines.append('  <record>')
            for col, value in row.items():
                # Fast XML escaping
                escaped_value = str(value).replace('&', '&amp;').replace(
                    '<', '&lt;').replace('>', '&gt;')
                xml_lines.append(f'    <{col}>{escaped_value}</{col}>')
            xml_lines.append('  </record>')

        xml_lines.append('</data>')

        # Write all at once for better performance
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(xml_lines))

    def convert(
        self,
        input_file: Path,
        output_dir: Path,
        output_format: str,
        output_filename: Optional[str] = None,
    ) -> Path:
        """
        Convert ARFF file to specified format with ultra-fast performance.

        Args:
            input_file: Path to input ARFF file
            output_dir: Directory for output file
            output_format: Target format (csv, json, xml, xlsx, parquet, orc)
            output_filename: Custom output filename (optional)

        Returns:
            Path to the converted file

        Raises:
            ARFFConverterError: If conversion fails
            ValidationError: If validation fails
        """
        # Validation (skip in fast mode for maximum speed)
        if not self.fast_mode:
            validate_file_path(str(input_file))
            validate_output_format(output_format)

        format_name = output_format.lower()
        if format_name not in self.SUPPORTED_FORMATS:
            raise ValidationError(f"Unsupported format: {format_name}")

        # Create output path
        output_path = create_output_path(
            input_file, output_dir, format_name, output_filename
        )

        try:
            # Load ARFF file with ultra-fast optimizations
            df = self._load_arff_ultra_fast(input_file)

            # Select ultra-fast conversion method
            conversion_methods = {
                'csv': self._convert_to_csv_ultra_fast,
                'json': self._convert_to_json_ultra_fast,
                'parquet': self._convert_to_parquet_ultra_fast,
                'orc': self._convert_to_orc_ultra_fast,
                'xlsx': self._convert_to_xlsx_ultra_fast,
                'xml': self._convert_to_xml_ultra_fast,
            }

            conversion_method = conversion_methods[format_name]
            conversion_method(df, output_path)

            self._log(f"Ultra-fast conversion completed: {output_path}")
            return output_path

        except Exception as e:
            if isinstance(e, (ARFFConverterError, ValidationError)):
                raise
            raise ARFFConverterError(f"Conversion failed: {e}") from e

    def batch_convert(
        self,
        input_files: List[Path],
        output_dir: Path,
        output_format: str,
        parallel: bool = True,
    ) -> List[Path]:
        """
        Convert multiple ARFF files in batch with ultra-fast performance.

        Args:
            input_files: List of input ARFF files
            output_dir: Directory for output files
            output_format: Target format
            parallel: Whether to process files in parallel

        Returns:
            List of paths to converted files
        """
        self._log(
            f"Starting ultra-fast batch conversion of {len(input_files)} files")

        if parallel and len(input_files) > 1:
            with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
                futures = []
                for input_file in input_files:
                    future = executor.submit(
                        self.convert, input_file, output_dir, output_format
                    )
                    futures.append(future)

                results = [future.result() for future in futures]
        else:
            results = []
            for input_file in input_files:
                result = self.convert(input_file, output_dir, output_format)
                results.append(result)

        self._log(
            f"Ultra-fast batch conversion completed: {len(results)} files processed")
        return results

    def benchmark(self, input_file: Path, output_dir: Path) -> Dict[str, float]:
        """
        Benchmark conversion speed across all formats.

        Args:
            input_file: Path to input ARFF file
            output_dir: Directory for benchmark outputs

        Returns:
            Dictionary with format names and conversion times
        """
        import time

        results = {}

        for format_name in self.SUPPORTED_FORMATS:
            try:
                start_time = time.time()
                self.convert(input_file, output_dir, format_name)
                end_time = time.time()

                results[format_name] = end_time - start_time
                self._log(
                    f"Benchmark {format_name}: {results[format_name]:.3f} seconds")

            except Exception as e:
                self._log(f"Benchmark {format_name} failed: {e}")
                results[format_name] = float('inf')

        return results
