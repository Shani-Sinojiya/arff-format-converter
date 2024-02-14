# Convert ARFF files to different formats.

![PyPI - Version](https://img.shields.io/pypi/v/arff-format-converter?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/arff-format-converter?style=flat-square)
![PyPI - License](https://img.shields.io/pypi/l/arff-format-converter?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/arff-format-converter?style=flat-square)
![GitHub Sponsors](https://img.shields.io/github/sponsors/Shani-Sinojiya)
![GitHub issues](https://img.shields.io/github/issues/Shani-Sinojiya/arff-format-converter?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Shani-Sinojiya/arff-format-converter?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Shani-Sinojiya/arff-format-converter?style=flat-square)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Shani-Sinojiya/arff-format-converter/CI?style=flat-square)
![GitHub followers](https://img.shields.io/github/followers/Shani-Sinojiya?style=social)
![GitHub forks](https://img.shields.io/github/forks/Shani-Sinojiya/arff-format-converter?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/Shani-Sinojiya/arff-format-converter?style=social)

The `arff-format-converter` tool allows you to convert ARFF files to various output formats. Below are the details:

## INSTALL

```bash
pip install arff-format-converter
```

## SYNOPSIS

```bash
arff-format-converter -f <file> -o <output_folder> -fmt <output_format>
```

## EXAMPLES

```bash
arff-format-converter -f data.arff -o output -fmt json
arff-format-converter -f data.arff -o output -fmt xml
arff-format-converter -f data.arff -o output -fmt csv
arff-format-converter -f data.arff -o output -fmt xlsx
arff-format-converter -f data.arff -o output -fmt orc
```

## OPTIONS

- `-f, --file` Path to the ARFF file.
- `-o, --output` Path to the output folder.
- `-fmt, --format` Output format: 'xml', 'json', 'csv', 'xlsx', 'orc'.

## SUPPORTED FORMATS

- **ARFF** (input)
- **XML** (output)
- **JSON** (output)
- **CSV** (output)
- **XLSX** (output)
- **ORC** (Apache ORC format) (output)

## AUTHOR

Written by [Shani Sinojiya](https://www.shanisinojiya.com).

## REPORTING BUGS:

Report bugs to [issue section](https://github.com/Shani-Sinojiya/arff-format-converter/issues)

**_Remember to replace `"data.arff"` with the actual path to your ARFF file and `"output"` with the desired output folder. Feel free to adapt this code snippet for other formats like XML, CSV, XLSX, or ORC as needed! 🚀_**

## Buy me a coffee ☕️

If you like my work, feel free to support it by buying me a coffee.

<a href="https://www.buymeacoffee.com/shanisinojiya" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
