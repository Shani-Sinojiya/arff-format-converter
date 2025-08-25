# Contributing to ARFF Format Converter 🚀

Thank you for your interest in contributing to ARFF Format Converter! This project emphasizes **ultra-high performance** and **reliability**.

## 📋 Quick Checklist

- [ ] Fork the repository
- [ ] Create a feature branch
- [ ] Include performance benchmarks
- [ ] Add/update tests (maintain 100% coverage)
- [ ] Run the full test suite
- [ ] Update documentation
- [ ] Submit a pull request

## 🚀 Performance First Development

### Performance Standards

**All contributions must:**

- Maintain or improve existing benchmark results
- Include before/after performance metrics
- Profile memory usage for large datasets
- Pass type checking with `mypy --strict`

### Before You Start

```bash
# Setup development environment
git clone https://github.com/Shani-Sinojiya/arff-format-converter.git
cd arff-format-converter

# Using uv (recommended - fastest setup)
uv sync
uv run pytest  # Verify everything works

# Or using traditional venv
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -e ".[dev]"
pytest
```

## 📊 Performance Testing

### Required Benchmarks

Before submitting any PR that touches core conversion logic:

```bash
# Run full benchmark suite
python scripts/benchmark_suite.py --full --output baseline.json

# After your changes
python scripts/benchmark_suite.py --full --output current.json

# Compare results (must show no regression)
python scripts/compare_performance.py baseline.json current.json
```

### Performance Profiling

```bash
# Memory profiling
python -m memory_profiler scripts/profile_memory.py

# CPU profiling
python -m cProfile -o profile.stats scripts/benchmark.py
python -c "import pstats; pstats.Stats('profile.stats').sort_stats('cumulative').print_stats(20)"
```

## 🧪 Testing Requirements

### Test Coverage

- **100% code coverage required**
- **Performance tests for any new features**
- **Edge case testing for data type handling**
- **Memory usage validation for large files**

### Running Tests

```bash
# Run all tests with coverage
uv run pytest --cov=arff_format_converter --cov-report=html

# Run only fast tests (during development)
pytest -m "not slow"

# Run performance tests
pytest -m "performance" -v

# Run specific test categories
pytest tests/test_core.py -v
pytest tests/test_cli.py -v
pytest tests/test_performance.py -v
```

### Writing New Tests

```python
# Example performance test
import pytest
from arff_format_converter import ARFFConverter
import time

def test_conversion_performance():
    """Test that conversion meets performance standards."""
    converter = ARFFConverter(fast_mode=True)

    start_time = time.time()
    result = converter.convert("test_data.arff", "output", "parquet")
    duration = time.time() - start_time

    # Performance assertion
    assert duration < 5.0, f"Conversion took {duration}s, expected <5s"
    assert result.file_size > 0
```

## 🔧 Code Quality Standards

### Type Safety

All code must pass strict type checking:

```bash
# Type checking
uv run mypy arff_format_converter/ --strict

# Required: Add type hints to all functions
def convert_data(input_file: Path, output_format: str) -> ConversionResult:
    """Convert data with proper type hints."""
    ...
```

### Code Formatting

```bash
# Format code before committing
uv run black arff_format_converter/
uv run isort arff_format_converter/

# Linting
uv run flake8 arff_format_converter/

# Or run all quality checks
uv run pre-commit run --all-files
```

### Documentation

- **Docstrings required for all public functions**
- **Performance notes in docstrings**
- **Type hints for all parameters and returns**
- **Update README.md if adding new features**

```python
def convert_arff(
    input_file: Path,
    output_format: str,
    fast_mode: bool = True
) -> ConversionResult:
    """Convert ARFF file to specified format with ultra-high performance.

    Args:
        input_file: Path to input ARFF file
        output_format: Target format ('csv', 'json', 'parquet', etc.)
        fast_mode: Enable optimizations (default: True for max speed)

    Returns:
        ConversionResult with timing and file information

    Performance:
        - Parquet: 50x faster than v1.x
        - JSON: 25x faster with orjson
        - CSV: 20x faster with polars

    Raises:
        FileNotFoundError: If input file doesn't exist
        UnsupportedFormatError: If format not supported
    """
```

## 🐛 Bug Reports

### Performance Regression Reports

If you discover a performance regression:

1. **Include benchmark comparison:**

   ```
   v2.0.0: 450ms for 10K rows to CSV
   current: 1200ms for 10K rows to CSV (2.67x slower!)
   ```

2. **Provide test case:**

   ```python
   # Minimal reproduction case
   converter = ARFFConverter(fast_mode=True)
   # This should be fast but isn't
   converter.convert("large_file.arff", "output", "csv")
   ```

3. **System information:**
   - Python version
   - OS and version
   - CPU and RAM specs
   - Storage type (SSD/HDD)

### General Bug Reports

Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md):

- Clear reproduction steps
- Expected vs actual behavior
- Sample data (if possible)
- Error messages and stack traces

## ✨ Feature Requests

### Performance-Focused Features

We prioritize features that:

- **Improve conversion speed**
- **Reduce memory usage**
- **Support larger datasets**
- **Add new high-performance formats**

### Feature Request Template

```markdown
## Feature Request: [Brief Description]

**Performance Impact:** Expected 2-5x speedup for large files

**Use Case:** Converting 1GB+ ARFF files for ML pipelines

**Implementation Ideas:**

- Use memory mapping for large files
- Implement parallel processing for chunks
- Add support for Apache Arrow format

**Benchmarks:**

- Current: 45s for 100MB file
- Expected: <10s with new feature
```

## 🎯 Priority Areas

### High Priority

- **Performance optimizations** (always welcome!)
- **Memory usage improvements**
- **New format support** (with benchmarks)
- **Large dataset handling**

### Medium Priority

- **CLI enhancements**
- **Error handling improvements**
- **Documentation updates**
- **Cross-platform compatibility**

### Lower Priority

- **Code style improvements** (unless performance impact)
- **Refactoring** (only if performance neutral)

## 📝 Pull Request Process

### 1. Before Submitting

```bash
# Ensure all checks pass
uv run pytest --cov=arff_format_converter
uv run mypy arff_format_converter/ --strict
uv run black --check arff_format_converter/
uv run isort --check-only arff_format_converter/

# Run performance benchmarks
python scripts/benchmark_suite.py --compare-with-baseline
```

### 2. PR Description Template

```markdown
## Performance Impact 🚀

**Benchmark Results:**

- CSV conversion: 15% faster
- Memory usage: 20% reduction
- Large files (>100MB): 2x speedup

**Before/After:**

- Old: 850ms for 10K rows
- New: 720ms for 10K rows

## Changes Made

- [ ] Core algorithm optimization
- [ ] Memory usage improvement
- [ ] New format support
- [ ] Bug fix
- [ ] Documentation update

## Testing

- [ ] All existing tests pass
- [ ] New tests added for changes
- [ ] Performance benchmarks included
- [ ] Memory profiling completed

## Breaking Changes

None / List any breaking changes
```

### 3. Review Process

1. **Automated checks** must pass (CI/CD)
2. **Performance benchmarks** reviewed
3. **Code review** by maintainers
4. **Documentation** review if applicable
5. **Merge** after approval

## 🤝 Community Guidelines

### Be Performance-Minded

- Always consider performance impact
- Profile before optimizing
- Measure twice, code once

### Be Collaborative

- Review others' PRs with performance focus
- Share benchmark results
- Help with performance debugging

### Be Professional

- Follow code of conduct
- Provide constructive feedback
- Focus on technical merit

## 📚 Resources

### Performance Optimization

- [Polars User Guide](https://pola-rs.github.io/polars-book/)
- [PyArrow Documentation](https://arrow.apache.org/docs/python/)
- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

### Testing & Quality

- [pytest Documentation](https://docs.pytest.org/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [Black Code Formatter](https://black.readthedocs.io/)

## 🏆 Recognition

Contributors who significantly improve performance will be:

- **Featured in release notes**
- **Added to README acknowledgments**
- **Invited to be project maintainers**

## 📞 Questions?

- **GitHub Discussions:** For general questions
- **GitHub Issues:** For bug reports and feature requests
- **Email:** shanisinojiya@gmail.com for maintainer contact

---

Thank you for contributing to the fastest ARFF converter in the Python ecosystem! 🚀
