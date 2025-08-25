---
name: ⚡ Performance Regression
about: Report a performance regression - conversion slower than expected
title: "[REGRESSION] "
labels: ["performance", "regression", "priority-high"]
assignees: ["Shani-Sinojiya"]
---

## ⚡ Performance Regression Report

**Severity:**

- [ ] Critical - 50%+ slower than previous version
- [ ] High - 25-50% slower
- [ ] Medium - 10-25% slower
- [ ] Low - <10% slower but noticeable

## 📊 Benchmark Comparison

**Previous performance (baseline):**

```
Version: X.X.X
Operation: Convert 10K rows to CSV
Time: 450ms
Memory: 25MB peak
```

**Current performance (regression):**

```
Version: X.X.X
Operation: Convert 10K rows to CSV
Time: 1200ms (2.67x slower!)
Memory: 45MB peak (80% increase)
```

**Performance delta:**

- Speed: XXx slower
- Memory: XX% more usage
- File size: XX% larger output (if applicable)

## 🔄 Reproduction

**Minimal reproduction code:**

```python
from arff_format_converter import ARFFConverter
import time

converter = ARFFConverter(fast_mode=True)

start = time.time()
result = converter.convert(
    "test_data.arff",
    "output",
    "csv"
)
duration = time.time() - start
print(f"Duration: {duration:.3f}s")
```

**Test data characteristics:**

- File size: XXX MB
- Rows: XXX,XXX
- Columns: XXX
- Data types: [numeric/string/mixed/datetime]
- Complexity: [simple/mixed/complex]

## 🔍 Investigation

**When did this start?**

- [ ] Specific version (which?)
- [ ] Recent commit (hash?)
- [ ] Gradual degradation
- [ ] Unknown

**Affected operations:**

- [ ] All conversions
- [ ] Specific format (CSV/JSON/Parquet/etc.)
- [ ] Large files only (>XXX MB)
- [ ] Specific data types
- [ ] Memory-constrained environments

**Configuration tested:**

```python
# Slow configuration
converter = ARFFConverter(
    fast_mode=True,
    parallel=True,
    chunk_size=10000
)

# Alternative configuration
converter = ARFFConverter(
    fast_mode=False,
    parallel=False,
    chunk_size=5000
)
```

## 💻 Environment

**System specs:**

- OS: [Windows 11/Ubuntu 22.04/macOS 13]
- CPU: [Intel i7-12700K, Apple M2, etc.]
- RAM: [16GB/32GB/etc.]
- Storage: [NVMe SSD/SATA SSD/HDD]
- Python: [3.10.8/3.11.5/etc.]

**Package versions:**

```bash
# Current installation
pip list | grep -E "(arff-format-converter|polars|pyarrow|pandas)"

# Or paste output of:
python -c "import arff_format_converter; print(arff_format_converter.__version__)"
```

## 🧪 Profiling Data

**CPU profiling (if available):**

```bash
# Run this and paste top functions
python -m cProfile -s cumulative -m arff_format_converter convert \
  --file test.arff --output output --format csv
```

**Memory profiling (if available):**

```bash
# Run this and paste peak memory usage
python -m memory_profiler profile_script.py
```

**Hot spots identified:**

<!-- List functions/methods that appear to be slow -->

## 🔧 Workarounds

**Temporary workarounds found:**

- [ ] Use different format
- [ ] Disable fast_mode
- [ ] Reduce chunk_size
- [ ] Use older version
- [ ] Other: ****\_\_\_****

**Acceptable performance with:**

```python
# Configuration that works acceptably
converter = ARFFConverter(
    # workaround settings
)
```

## 📈 Impact Assessment

**Business impact:**

- [ ] Blocks production use
- [ ] Significantly slows pipeline
- [ ] Minor inconvenience
- [ ] Testing/development only

**Dataset size affected:**

- [ ] All sizes
- [ ] Small files (<1MB)
- [ ] Medium files (1-100MB)
- [ ] Large files (>100MB)
- [ ] Huge files (>1GB)

## 🎯 Expected Resolution

**Performance target:**

- Should achieve: XXX ms for XXX rows
- Previous baseline: XXX ms
- Acceptable threshold: XXX ms (within XX% of baseline)

**Priority level:**

- [ ] Fix in hotfix (critical production issue)
- [ ] Fix in next patch release
- [ ] Fix in next minor release
- [ ] Fix when convenient

## 📊 Additional Data

**Comparison with alternatives:**

```
Our tool (current): 1200ms
Our tool (baseline): 450ms
pandas native: 800ms
Other tools: XXXms
```

**Related reports:**

<!-- Link to any related performance issues -->

**Additional context:**

<!-- Any other relevant information -->

---

**For Maintainers - Performance Investigation Checklist:**

- [ ] Reproduced locally
- [ ] Profiled with cProfile
- [ ] Profiled with memory_profiler
- [ ] Identified regression commit
- [ ] Created benchmark test
- [ ] Performance fix implemented
- [ ] Regression test added
