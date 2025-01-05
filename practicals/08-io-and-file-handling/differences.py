#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f1, open(sys.argv[2], 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
    for i, (line1, line2) in enumerate(zip(lines1, lines2), 1):
        if line1.strip() != line2.strip():
            print(f"Difference at line {i}:")
            print(f"File 1: {line1.strip()}")
            print(f"File 2: {line2.strip()}")
