"""Configuration and constants for ARFF Format Converter."""

from typing import Set

# Supported output formats
SUPPORTED_FORMATS: Set[str] = {
    "csv", "json", "xml", "xlsx", "parquet", "orc"
}

# Default settings
DEFAULT_CHUNK_SIZE = 10000
DEFAULT_MAX_WORKERS = None  # Let system decide
DEFAULT_ENCODING = "utf-8"
FALLBACK_ENCODING = "latin-1"

# Performance settings
FAST_MODE_CHUNK_SIZE = 50000
# Minimum rows to consider parallel processing
PARALLEL_PROCESSING_THRESHOLD = 1000

# File size thresholds (in MB)
SMALL_FILE_THRESHOLD = 10
LARGE_FILE_THRESHOLD = 100

# Memory management
DEFAULT_MEMORY_LIMIT_MB = 1024
MEMORY_SAFETY_FACTOR = 0.8  # Use 80% of available memory

# Output file naming
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"

# Legacy constants for backward compatibility
legal_formats = list(SUPPORTED_FORMATS)
