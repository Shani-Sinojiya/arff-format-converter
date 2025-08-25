"""Text constants and messages for ARFF Format Converter."""

bottom_msg = '''SUPPORTED FORMATS:
    - ARFF (input)
    - XML (output)
    - JSON (output)
    - CSV (output)
    - XLSX (output)
    - ORC (Apache ORC format) (output)
    - Parquet (output)

FEATURES:
    - High-performance conversion with parallel processing
    - Memory-efficient chunked processing for large files
    - UV package manager support
    - Rich CLI with progress bars and beautiful output
    - Fast mode for production use
    - Comprehensive error handling and validation

AUTHOR:
    Written by Shani Sinojiya <https://www.shanisinojiya.tech>

REPORTING BUGS:
    Report bugs to <https://github.com/Shani-Sinojiya/arff-format-converter/issues>

COPYRIGHT:
    Creative Commons Attribution-NoDerivatives 4.0 International Public License
    All Rights Reserved By Shani Sinojiya

MODERN CLI:
    For enhanced features, use the modern CLI:
    arff-format-converter convert --file input.arff --output ./output --format csv
    arff-format-converter info
    arff-format-converter benchmark --file input.arff
'''

# Modern help messages
CONVERSION_HELP = """
🚀 ARFF Format Converter v2.0 - High Performance File Conversion

Convert ARFF files to various formats with modern Python features:
• Fast parallel processing for large datasets
• Memory-efficient chunked processing
• Beautiful progress indicators with Rich
• UV package manager support
• Type-safe code with full type hints

Examples:
  arff-format-converter convert -f data.arff -o output -fmt csv --fast
  arff-format-converter convert -f large.arff -o output -fmt parquet --parallel
  arff-format-converter benchmark -f data.arff --formats csv,json,parquet
"""

FORMAT_DESCRIPTIONS = {
    "csv": "Comma-separated values - Fast, widely supported",
    "json": "JavaScript Object Notation - Web-friendly, structured",
    "xml": "Extensible Markup Language - Hierarchical, verbose",
    "xlsx": "Excel spreadsheet - Business-friendly, feature-rich",
    "parquet": "Columnar storage - High performance, efficient compression",
    "orc": "Optimized Row Columnar - Big data optimized, very fast",
}

PERFORMANCE_TIPS = """
💡 Performance Tips:

1. Use --fast mode to skip validation checks
2. Enable --parallel for large files (>10MB)
3. Use Parquet or ORC formats for best performance
4. Adjust --chunk-size for memory optimization
5. Use UV for fastest package management: `uv add arff-format-converter`
"""
