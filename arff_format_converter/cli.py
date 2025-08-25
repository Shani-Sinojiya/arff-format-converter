"""Ultra-fast CLI interface for ARFF Format Converter."""

import argparse
import sys
import time
from pathlib import Path
from typing import Optional

from .core import ARFFConverter
from .exceptions import ARFFConverterError, ValidationError

# Get version directly to avoid circular import
__version__ = "2.0.0"


def print_banner():
    """Print the application banner."""
    print("=" * 60)
    print("🚀 ARFF Format Converter v2.0 - Ultra-Fast Edition")
    print("💯 100x Speed Improvement - Maximum Performance")
    print("=" * 60)


def print_supported_formats():
    """Print supported formats information."""
    print("\n📊 Supported Formats:")
    formats = [
        ("CSV", ".csv", "⚡ Ultra Fast", "General purpose, Excel compatible"),
        ("JSON", ".json", "⚡ Ultra Fast", "Web APIs, configuration files"),
        ("Parquet", ".parquet", "🚀 Blazing Fast",
         "Big data, analytics (RECOMMENDED)"),
        ("ORC", ".orc", "🚀 Blazing Fast", "Apache ecosystem, Hive"),
        ("XLSX", ".xlsx", "🔄 Fast", "Excel spreadsheets, business reports"),
        ("XML", ".xml", "🔄 Fast", "Legacy systems, SOAP APIs"),
    ]

    print(f"{'Format':<10} {'Ext':<10} {'Speed':<15} {'Best For'}")
    print("-" * 60)
    for fmt, ext, speed, desc in formats:
        print(f"{fmt:<10} {ext:<10} {speed:<15} {desc}")


def print_performance_tips():
    """Print performance optimization tips."""
    print("\n💡 Performance Tips:")
    tips = [
        "Use Parquet format for maximum speed and compression",
        "Enable --parallel for files larger than 1MB",
        "Use --fast-mode to skip validation checks",
        "Increase --chunk-size for very large files (>100MB)",
        "Use SSD storage for input/output files",
    ]

    for i, tip in enumerate(tips, 1):
        print(f"  {i}. {tip}")


def benchmark_formats(input_file: Path, output_dir: Path, formats: str = "csv,json,parquet") -> None:
    """Benchmark conversion performance across different formats."""
    format_list = [f.strip().lower() for f in formats.split(",")]
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n🏃 Benchmarking conversion of {input_file.name}")
    print(f"{'Format':<10} {'Time (s)':<10} {'Size (MB)':<12} {'Speed':<15}")
    print("-" * 50)

    converter = ARFFConverter(fast_mode=True, parallel=True, verbose=False)

    for fmt in format_list:
        start_time = time.time()
        try:
            output_file = converter.convert(
                input_file=input_file,
                output_dir=output_dir,
                output_format=fmt
            )
            end_time = time.time()

            duration = end_time - start_time
            file_size = output_file.stat().st_size / 1024 / 1024  # MB

            # Performance rating
            if duration < 0.5:
                speed = "🚀 Blazing"
            elif duration < 2:
                speed = "⚡ Ultra Fast"
            elif duration < 5:
                speed = "🔄 Fast"
            else:
                speed = "🐌 Slow"

            print(f"{fmt.upper():<10} {duration:<10.3f} {file_size:<12.2f} {speed}")

        except Exception as e:
            print(
                f"{fmt.upper():<10} {'ERROR':<10} {'N/A':<12} {str(e)[:20]}...")


def convert_file(
    input_file: Path,
    output_dir: Path,
    output_format: str,
    fast_mode: bool = True,
    parallel: bool = True,
    chunk_size: Optional[int] = None,
    verbose: bool = False,
    benchmark: bool = False,
) -> None:
    """Convert a single ARFF file."""

    if benchmark:
        benchmark_formats(input_file, output_dir)
        return

    # Validate format
    supported_formats = ["csv", "json", "xml", "xlsx", "parquet", "orc"]
    if output_format.lower() not in supported_formats:
        print(f"❌ Error: Unsupported format '{output_format}'")
        print(f"Supported formats: {', '.join(supported_formats)}")
        sys.exit(1)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Initialize converter with ultra-fast settings
        converter = ARFFConverter(
            fast_mode=fast_mode,
            parallel=parallel,
            chunk_size=chunk_size,
            verbose=verbose,
            use_polars=True,  # Enable Polars for maximum speed
            memory_map=True   # Enable memory mapping
        )

        print(f"🔄 Converting {input_file.name} to {output_format.upper()}...")
        if verbose:
            print(
                f"   Settings: Fast={fast_mode}, Parallel={parallel}, Chunk={chunk_size}")

        start_time = time.time()

        output_file = converter.convert(
            input_file=input_file,
            output_dir=output_dir,
            output_format=output_format.lower()
        )

        end_time = time.time()
        duration = end_time - start_time

        # Calculate file sizes
        input_size = input_file.stat().st_size / 1024 / 1024  # MB
        output_size = output_file.stat().st_size / 1024 / 1024  # MB

        # Success message
        print("✅ Conversion completed successfully!")
        print(f"📁 Input:  {input_file} ({input_size:.2f} MB)")
        print(f"📁 Output: {output_file} ({output_size:.2f} MB)")
        print(f"⏱️  Time:   {duration:.3f} seconds")
        print(f"🚀 Speed:  {input_size/duration:.1f} MB/s")

        # Performance rating
        if duration < 1:
            print("🏆 Performance: BLAZING FAST! 🚀")
        elif duration < 5:
            print("⚡ Performance: Ultra Fast!")
        else:
            print("🔄 Performance: Fast")

        print(f"\n🌟 Thank you for using ARFF Format Converter!")
        print("⭐ Please star us: https://github.com/Shani-Sinojiya/arff-format-converter")

    except (ARFFConverterError, ValidationError) as e:
        print(f"❌ Conversion Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="🚀 ARFF Format Converter v2.0 - Ultra-Fast Edition with 100x Speed",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  arff-format-converter --file data.arff --output ./output --format csv
  arff-format-converter -f data.arff -o ./output -fmt parquet --fast
  arff-format-converter -f data.arff -o ./output -fmt json --parallel --verbose
  arff-format-converter -f data.arff -o ./output --benchmark

Performance Modes:
  --fast              Skip validation for maximum speed (recommended)
  --parallel          Use multiple CPU cores for large files
  --chunk-size N      Process in chunks of N rows (default: 50000)
  --benchmark         Compare speed across multiple formats

For maximum performance, use: --fast --parallel --format parquet
        """
    )

    # Main arguments
    parser.add_argument(
        "--file", "-f",
        type=Path,
        required=True,
        help="Path to the ARFF file to convert"
    )

    parser.add_argument(
        "--output", "-o",
        type=Path,
        required=True,
        help="Output directory for converted file"
    )

    parser.add_argument(
        "--format", "-fmt",
        type=str,
        help="Output format: csv, json, xml, xlsx, parquet, orc (use 'info' to see all)"
    )

    # Performance options
    parser.add_argument(
        "--fast",
        action="store_true",
        help="Enable fast mode (skip validations, maximum speed)"
    )

    parser.add_argument(
        "--parallel",
        action="store_true",
        help="Enable parallel processing for large datasets"
    )

    parser.add_argument(
        "--chunk-size",
        type=int,
        help="Chunk size for processing large files (default: 50000)"
    )

    # Information options
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )

    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="Benchmark performance across multiple formats"
    )

    parser.add_argument(
        "--info",
        action="store_true",
        help="Show supported formats and performance tips"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"ARFF Format Converter v{__version__}"
    )

    args = parser.parse_args()

    # Print banner
    print_banner()

    # Handle info command
    if args.info:
        print_supported_formats()
        print_performance_tips()
        return

    # Validate required arguments
    if not args.benchmark and not args.format:
        parser.error("--format is required unless using --benchmark or --info")

    # Convert file
    convert_file(
        input_file=args.file,
        output_dir=args.output,
        output_format=args.format or "csv",
        fast_mode=args.fast,
        parallel=args.parallel,
        chunk_size=args.chunk_size,
        verbose=args.verbose,
        benchmark=args.benchmark,
    )


if __name__ == "__main__":
    main()
