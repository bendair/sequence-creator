#!/usr/bin/env python3

import sys
import os

def main():
    """
    sequence-creator.py: A script to create multiple files of a given size,
    filled with random data, with specified file prefix, extension, 
    and optional zero-padded numbering.

    Usage:
      python sequence-creator.py <prefix> <extension> <size_in_bytes> <count> [zero_pad]

    Parameters:
      <prefix>       : Base name for the files (e.g., "file", "test").
      <extension>    : Extension for the files (e.g., "txt").
      <size_in_bytes>: Exact size for each file in bytes (e.g., 1024).
      <count>        : How many files to create.
      [zero_pad]     : (Optional) Number of digits for zero-padding.
                       If omitted or 0, no padding is applied.

    Examples:
      1) Create 5 files with prefix 'myfile', extension 'txt', each 1024 bytes,
         with no zero-padding:
            python sequence-creator.py myfile txt 1024 5

         This produces:
            myfile_1.txt
            myfile_2.txt
            myfile_3.txt
            myfile_4.txt
            myfile_5.txt

      2) Create 5 files with prefix 'myfile', extension 'txt', each 1024 bytes,
         zero-padded to 3 digits:
            python sequence-creator.py myfile txt 1024 5 3

         This produces:
            myfile_001.txt
            myfile_002.txt
            myfile_003.txt
            myfile_004.txt
            myfile_005.txt
    """

    if len(sys.argv) < 5:
        print("Usage: python sequence-creator.py <prefix> <extension> <size_in_bytes> <count> [zero_pad]")
        sys.exit(1)

    prefix = sys.argv[1]
    extension = sys.argv[2]
    try:
        size = int(sys.argv[3])
    except ValueError:
        print("Error: size_in_bytes must be an integer.")
        sys.exit(1)
    try:
        count = int(sys.argv[4])
    except ValueError:
        print("Error: count must be an integer.")
        sys.exit(1)

    if len(sys.argv) > 5:
        try:
            zero_pad = int(sys.argv[5])
        except ValueError:
            print("Error: zero_pad must be an integer.")
            sys.exit(1)
    else:
        zero_pad = 0

    for i in range(1, count + 1):
        # Create a zero-padded string if zero_pad > 0, otherwise just use i
        if zero_pad > 0:
            index_str = str(i).zfill(zero_pad)
        else:
            index_str = str(i)

        filename = f"{prefix}_{index_str}.{extension}"
        print(f"Creating file: {filename} ({size} bytes) with random data")

        # To minimize memory usage for large files, write in chunks
        # If size is small, you can do it in one go: f.write(os.urandom(size))
        with open(filename, 'wb') as f:
            bytes_written = 0
            chunk_size = 65536  # 64KB per chunk
            while bytes_written < size:
                to_write = min(chunk_size, size - bytes_written)
                f.write(os.urandom(to_write))
                bytes_written += to_write

    print(f"Done! Created {count} file(s) with prefix '{prefix}', extension '{extension}', "
          f"and size {size} bytes each.")

if __name__ == "__main__":
    main()
