---
name: 🐛 Bug Report
about: Report a bug to help us improve performance and reliability
title: "[BUG] "
labels: ["bug", "needs-triage"]
assignees: ["Shani-Sinojiya"]
---

## 🐛 Bug Description

**Clear description of the bug:**

<!-- A clear and concise description of what the bug is -->

**Expected behavior:**

<!-- What should happen -->

**Actual behavior:**

<!-- What actually happens -->

## 🚀 Performance Impact

**Is this a performance regression?**

- [ ] Yes - conversion is slower than expected
- [ ] No - functional bug only
- [ ] Unknown

**If performance regression, provide benchmarks:**

```
Previous version: X.X.X took 450ms
Current version: X.X.X takes 1200ms (2.67x slower)
```

## 🔄 Reproduction Steps

**Minimal code to reproduce:**

```python
from arff_format_converter import ARFFConverter

# Add minimal reproduction code here
converter = ARFFConverter()
result = converter.convert("test.arff", "output", "csv")
```

**Steps to reproduce:**

1. Install version X.X.X
2. Run command/code above
3. Observe error/slowness

**Sample data (if possible):**

<!-- Attach small sample ARFF file or describe data structure -->

- File size: XXX MB
- Number of rows: XXX
- Number of attributes: XXX
- Data types: numeric/string/mixed

## 💻 Environment

**System Information:**

- OS: [e.g., Windows 11, Ubuntu 22.04, macOS 13]
- Python version: [e.g., 3.11.5]
- Package version: [e.g., 2.0.0]
- Installation method: [pip, uv, conda]

**Hardware:**

- CPU: [e.g., Intel i7-12700K]
- RAM: [e.g., 32GB]
- Storage: [e.g., NVMe SSD, HDD]

**Dependencies (if relevant):**

```bash
pip list | grep -E "(polars|pyarrow|pandas)"
```

## 📋 Error Details

**Error message:**

```
Paste full error message and stack trace here
```

**Log output (with --verbose):**

```
Run with --verbose flag and paste relevant log output
```

## 🧪 Testing

**Have you tried:**

- [ ] Different output formats
- [ ] Smaller test files
- [ ] Disabling fast_mode
- [ ] Different chunk_size values
- [ ] Running with --verbose

**Workaround found:**

<!-- If you found a workaround, please describe it -->

## 📊 Additional Context

**Configuration used:**

```python
converter = ARFFConverter(
    fast_mode=True,     # or False
    parallel=True,      # or False
    chunk_size=10000,   # or other value
    # ... other settings
)
```

**Related issues:**

<!-- Link any related issues -->

**Screenshots:**

<!-- If applicable, add screenshots to help explain your problem -->

---

**Checklist:**

- [ ] I have searched existing issues
- [ ] I have provided minimal reproduction code
- [ ] I have included system information
- [ ] I have tested with the latest version
- [ ] I have included error messages/stack traces
