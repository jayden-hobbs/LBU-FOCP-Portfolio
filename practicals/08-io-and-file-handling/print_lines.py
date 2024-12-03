#!/usr/bin/env python3

if __name__ == '__main__':
    filename = 'program1.txt'
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, 1):
            print(f"{line_number}\t{line.strip()}")



