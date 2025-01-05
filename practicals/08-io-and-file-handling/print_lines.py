#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, 1):
            print(f"{line_number}\t{line.strip()}")



