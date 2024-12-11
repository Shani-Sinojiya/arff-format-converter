# ARFF Format Converter

![PyPI - Version](https://img.shields.io/pypi/v/arff-format-converter?style=for-the-badge)
![PyPI - License](https://img.shields.io/pypi/l/arff-format-converter?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/arff-format-converter?style=for-the-badge)
![GitHub Sponsors](https://img.shields.io/github/sponsors/Shani-Sinojiya?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Shani-Sinojiya/arff-format-converter?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/Shani-Sinojiya/arff-format-converter?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/Shani-Sinojiya/arff-format-converter?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/Shani-Sinojiya/arff-format-converter?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/Shani-Sinojiya/arff-format-converter?style=for-the-badge)

The `arff-format-converter` tool allows you to convert ARFF files to various output formats. Below are the details:

## Table of Contents

- [Install](#install)
- [Synopsis](#synopsis)
- [Examples](#examples)
- [Options](#options)
- [Supported Formats](#supported-formats)
- [Author](#author)
- [Contributing](#contributing)
- [Features](#features)
- [License](#license)

## Install

```bash
pip install arff-format-converter
```

## Synopsis

```bash
arff-format-converter -f <file> -o <output_folder> -fmt <output_format> [--fast]
```

## Examples

```bash
arff-format-converter -f data.arff -o output -fmt json
arff-format-converter -f data.arff -o output -fmt xml
arff-format-converter -f data.arff -o output -fmt csv
arff-format-converter -f data.arff -o output -fmt xlsx
arff-format-converter -f data.arff -o output -fmt orc
arff-format-converter -f data.arff -o output -fmt parquet
arff-format-converter -f data.arff -o output -fmt json --fast
```

## Options

- `-f, --file` Path to the ARFF file.
- `-o, --output` Path to the output folder.
- `-fmt, --format` Output format: `xml`, `json`, `csv`, `xlsx`, `orc`, `parquet`.
- `--fast` Enable **fast mode**. Performs the conversion.

## Supported Formats

- **ARFF** (input)
- **XML** (output)
- **JSON** (output)
- **CSV** (output)
- **XLSX** (output)
- **ORC** (Apache ORC format) (output)
- **Parquet** (output)

## Author

Written by [Shani Sinojiya](https://www.shanisinojiya.tech).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request, or check the [issues section](https://github.com/Shani-Sinojiya/arff-format-converter/issues) for tasks that need help.

## Features

- Convert `.arff` files into multiple formats: `XML`, `JSON`, `CSV`, `XLSX`, `ORC`, and now `Parquet`.
- CLI-based, easy-to-use interface.
- Handles large datasets efficiently.
- Supports automated error handling and detailed logs.
- **Fast mode**: Skip validation checks for quicker conversions.

## License

This project is licensed under the [Creative Commons Attribution-NoDerivatives 4.0 International Public License](./LICENSE).
