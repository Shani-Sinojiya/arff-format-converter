"""ARFF Format Converter - Ultra-high-performance tool for converting ARFF files."""

__version__ = "2.0.0"
__author__ = "Shani Sinojiya"
__email__ = "shanisinojiya@gmail.com"
__license__ = "CC BY-ND 4.0"

from .core import ARFFConverter

__all__ = ["ARFFConverter", "__version__"]
