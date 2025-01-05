#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_characters = sum(len(line) for line in lines)
    
    print(f"Lines: {num_lines}")
    print(f"Words: {num_words}")
    print(f"Characters: {num_characters}")
    