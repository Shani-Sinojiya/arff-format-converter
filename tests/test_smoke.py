"""Simple smoke tests for basic functionality."""

import pytest
from arff_format_converter import ARFFConverter


def test_import():
    """Test that the package can be imported."""
    assert ARFFConverter is not None


def test_initialization():
    """Test basic initialization."""
    converter = ARFFConverter()
    assert converter is not None
    assert converter.fast_mode is False


def test_initialization_with_params():
    """Test initialization with parameters."""
    converter = ARFFConverter(fast_mode=True, parallel=True)
    assert converter.fast_mode is True
    assert converter.parallel is True


if __name__ == "__main__":
    test_import()
    test_initialization() 
    test_initialization_with_params()
    print("✅ All smoke tests passed!")
