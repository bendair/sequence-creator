# Sequence Creator

sequence-creator.py: 

A script to create multiple files of a given size, filled with random data, with specified file prefix, extension, 
and optional zero-padded numbering.

## Usage
python sequence-creator.py <prefix> <extension> <size_in_bytes> <count> [zero_pad]

## Parameters:
* prefix       : Base name for the files (e.g., "file", "test").
* extension    : Extension for the files (e.g., "txt").
* size_in_bytes : Exact size for each file in bytes (e.g., 1024).
* count>        : How many files to create.
* [zero_pad]     : (Optional) Number of digits for zero-padding. If omitted or 0, no padding is applied.

## Examples: 

1) Create 5 files with prefix 'myfile', extension 'txt', each 1024 bytes, with no zero-padding:
   
```
python sequence-creator.py myfile txt 1024 5
```

This produces:
            myfile_1.txt
            myfile_2.txt
            myfile_3.txt
            myfile_4.txt
            myfile_5.txt

2) Create 5 files with prefix 'myfile', extension 'txt', each 1024 bytes, zero-padded to 3 digits:

```
python sequence-creator.py myfile txt 1024 5 3
```

This produces:
            myfile_001.txt
            myfile_002.txt
            myfile_003.txt
            myfile_004.txt
            myfile_005.txt
  
