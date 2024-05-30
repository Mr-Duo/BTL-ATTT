@echo off
python encrypt.py ^
    --algorithms sha256 ^
    --text "The quick brown fox jumps over the lazy dog" ^
    --output_path output ^
    --output_file output.txt