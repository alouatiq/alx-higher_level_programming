#!/usr/bin/python3
"""Script that reads stdin line by
line and computes metrics."""
import sys

file_size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

try:
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()
        if len(parts) > 2:
            file_size += int(parts[-1])
            code = parts[-2]
            if code in valid_codes:
                status_codes[code] = status_codes.get(code, 0) + 1

        if i % 10 == 0:
            print("File size: {}".format(file_size))
            for code in sorted(status_codes):
                print("{}: {}".format(code, status_codes[code]))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(file_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))
