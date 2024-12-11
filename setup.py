from setuptools import setup, find_packages

version = '1.1.1'
name = 'arff-format-converter'
description = 'Converts ARFF files to CSV, JSON, XML, XLSX, ORC, and parquet.'
author = 'Shani Sinojiya'
author_email = 'shanisinojiya@gmail.com'

keywords = [
    "arff",
    "data-conversion",
    "format-conversion",
    "data-interchange",
    "machine-learning",
    "data-preprocessing",
    "data-transformation",
    "file-format-conversion",
    "data-science",
    "python-package",
    "xml",
    "json",
    "csv",
    "excel",
    "orc",
    "parquet",
    "pandas",
    "pyarrow",
    "data-manipulation",
    "data-export",
    "data-import",
]

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
        setup(
            name=name,
            version=version,
            packages=find_packages(),
            description=description,
            author=author,
            author_email=author_email,
            maintainer=author,
            maintainer_email=author_email,
            license="Creative Commons Attribution-NoDerivatives 4.0 International Public License",
            long_description=long_description,
            long_description_content_type='text/markdown',
            install_requires=[
                "argparse",
                "pandas",
                "pyarrow",
                "scipy"
            ],
            entry_points={
                'console_scripts': [
                    'arff-format-converter=arff_format_converter.arff_converter:main',
                ],
            },
            keywords=keywords,
            classifiers=[
                'Programming Language :: Python :: 3',
                'License :: OSI Approved :: Creative Commons Attribution-NoDerivatives 4.0 International Public License',
                'Operating System :: OS Independent',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'Programming Language :: Python :: 3 :: Only',
                'Natural Language :: English',
            ],
        )
except FileNotFoundError:
    print("Error: Readme File is not Found.")
