# iges_md5

# iges_md5

Get an MD5 checksum of a file. For IGES files, the header can be ignored so that we obtain a checksum for the geometry only.

## Installation

```bash
pip install git+https://github.com/joergbrech/iges_md5
```

## Usage

The following command simply returns the MD5 Checksum of an ASCII file
```bash
iges_md5 input_file.iges
```

The following file ignores the HEADER, if the input file is an IGES file
```bash
iges_md5 input_file.iges --ignore-header
```