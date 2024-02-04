# Convert ARFF files to different formats.

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
