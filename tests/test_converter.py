"""Test suite for ARFF Format Converter."""

import pytest
import tempfile
from pathlib import Path
import pandas as pd

from arff_format_converter import ARFFConverter
from arff_format_converter.exceptions import ValidationError, ARFFConverterError


class TestARFFConverter:
    """Test the ARFFConverter class."""

    @pytest.fixture
    def sample_arff_content(self):
        """Sample ARFF file content for testing."""
        return """@relation test_data

@attribute feature1 numeric
@attribute feature2 string
@attribute class {positive,negative}

@data
1.0,hello,positive
2.0,world,negative
3.0,test,positive
"""

    @pytest.fixture
    def sample_arff_file(self, sample_arff_content):
        """Create a temporary ARFF file for testing."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.arff', delete=False) as f:
            f.write(sample_arff_content)
            temp_path = Path(f.name)

        yield temp_path

        # Cleanup
        if temp_path.exists():
            temp_path.unlink()

    @pytest.fixture
    def output_dir(self):
        """Create a temporary output directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield Path(temp_dir)

    def test_converter_initialization(self):
        """Test ARFFConverter initialization."""
        converter = ARFFConverter()
        assert converter.fast_mode is False
        assert converter.parallel is False
        assert converter.verbose is False

        converter_fast = ARFFConverter(
            fast_mode=True, parallel=True, verbose=True)
        assert converter_fast.fast_mode is True
        assert converter_fast.parallel is True
        assert converter_fast.verbose is True

    def test_convert_to_csv(self, sample_arff_file, output_dir):
        """Test conversion to CSV format."""
        converter = ARFFConverter()

        output_file = converter.convert(
            input_file=sample_arff_file,
            output_dir=output_dir,
            output_format="csv"
        )

        assert output_file.exists()
        assert output_file.suffix == ".csv"

        # Verify content
        df = pd.read_csv(output_file)
        assert len(df) == 3
        assert "feature1" in df.columns
        assert "feature2" in df.columns
        assert "class" in df.columns

    def test_convert_to_json(self, sample_arff_file, output_dir):
        """Test conversion to JSON format."""
        converter = ARFFConverter()

        output_file = converter.convert(
            input_file=sample_arff_file,
            output_dir=output_dir,
            output_format="json"
        )

        assert output_file.exists()
        assert output_file.suffix == ".json"

        # Verify content
        df = pd.read_json(output_file)
        assert len(df) == 3

    def test_convert_to_parquet(self, sample_arff_file, output_dir):
        """Test conversion to Parquet format."""
        converter = ARFFConverter()

        output_file = converter.convert(
            input_file=sample_arff_file,
            output_dir=output_dir,
            output_format="parquet"
        )

        assert output_file.exists()
        assert output_file.suffix == ".parquet"

        # Verify content
        df = pd.read_parquet(output_file)
        assert len(df) == 3

    def test_fast_mode(self, sample_arff_file, output_dir):
        """Test fast mode conversion."""
        converter = ARFFConverter(fast_mode=True)

        output_file = converter.convert(
            input_file=sample_arff_file,
            output_dir=output_dir,
            output_format="csv"
        )

        assert output_file.exists()

    def test_invalid_format(self, sample_arff_file, output_dir):
        """Test conversion with invalid format."""
        converter = ARFFConverter()

        with pytest.raises(ValidationError):
            converter.convert(
                input_file=sample_arff_file,
                output_dir=output_dir,
                output_format="invalid"
            )

    def test_nonexistent_file(self, output_dir):
        """Test conversion with non-existent file."""
        converter = ARFFConverter()
        nonexistent_file = Path("nonexistent.arff")

        with pytest.raises((ValidationError, ARFFConverterError)):
            converter.convert(
                input_file=nonexistent_file,
                output_dir=output_dir,
                output_format="csv"
            )

    def test_custom_filename(self, sample_arff_file, output_dir):
        """Test conversion with custom filename."""
        converter = ARFFConverter()

        output_file = converter.convert(
            input_file=sample_arff_file,
            output_dir=output_dir,
            output_format="csv",
            output_filename="custom_name.csv"
        )

        assert output_file.exists()
        assert output_file.name == "custom_name.csv"


class TestUtilityFunctions:
    """Test utility functions."""

    def test_validate_file_path(self):
        """Test file path validation."""
        from arff_format_converter.utils import validate_file_path

        # Test with non-existent file
        with pytest.raises(ValidationError):
            validate_file_path(Path("nonexistent.arff"))

    def test_validate_output_format(self):
        """Test output format validation."""
        from arff_format_converter.utils import validate_output_format

        # Valid formats
        validate_output_format("csv")
        validate_output_format("json")
        validate_output_format("parquet")

        # Invalid format
        with pytest.raises(ValidationError):
            validate_output_format("invalid")

    def test_format_duration(self):
        """Test duration formatting."""
        from arff_format_converter.utils import format_duration

        assert "ms" in format_duration(0.5)
        assert "s" in format_duration(5.5)
        assert "m" in format_duration(65.5)


if __name__ == "__main__":
    pytest.main([__file__])
