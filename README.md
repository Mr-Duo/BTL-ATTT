# [BTL-ATTT]
# CLI Tool to demonstrate SHA algorithms

## Overview
This is a command line interface tool to demonstrate how Secure Hash Algorithms (SHA) works.
This tool supports SHA1, SHA2 and SHA3 algorithms families.

## Installation
Clone the repository:
```bat
git clone https://github.com/Mr-Duo/BTL-ATTT
cd BTL-ATTT
```

## Usage
### Windows Environment (RECOMMENDED)
- **Encrypt from text file**
```bash
python encrypt.py ^
     --algorithms <sha1/sha256/...> ^
     --input_path <path/to/input/folder> ^
     --input_file <input_file.txt> ^
     --output_path <path/to/output/folder> ^
     --output_file <output_file.txt>
```

- **Encrypt from user input**
```bash
python encrypt.py ^
     --algorithms <sha1/sha256/...> ^
     --text <PUT YOUR TEXT HERE> ^
     --output_path <path/to/output/folder> ^
     --output_file <output_file.txt>
```

***Visit examples folder for more detail scripts***

## Our team
- **[Nguyen Dang Duong](https://github.com/Mr-Duo)** 
- **[Pham Trung Hieu](https://github.com/iammhiru)** 