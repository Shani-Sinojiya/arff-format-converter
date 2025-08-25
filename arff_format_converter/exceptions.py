"""Custom exceptions for ARFF Format Converter."""


class ARFFConverterError(Exception):
    """Base exception for ARFF Converter errors."""
    pass


class ValidationError(ARFFConverterError):
    """Exception raised for validation errors."""
    pass


class FileFormatError(ARFFConverterError):
    """Exception raised for file format errors."""
    pass


class ConversionError(ARFFConverterError):
    """Exception raised during conversion process."""
    pass


class UnsupportedFormatError(ARFFConverterError):
    """Exception raised for unsupported output formats."""
    pass
