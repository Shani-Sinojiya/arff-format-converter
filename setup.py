from setuptools import setup, find_packages

version = '1.0.3'
name = 'arff-format-converter'
description = 'Converts ARFF files to CSV, JSON, XML, XLSX, and ORC'
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
    "pandas",
    "pyarrow",
    "data-manipulation",
    "data-export",
    "data-import",
]

setup(
    name=name,
    version=version,
    packages=find_packages(),
    description=description,
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    license="MIT",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "ujson",
        "pandas",
        "argparse",
        "tqdm",
        "fastavro",
        "openpyxl",
    ],
    entry_points={
        'console_scripts': [
            'arff-format-converter=arff_format_converter.arff_converter:main',
        ],
    },
    keywords=keywords,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
