#!/usr/bin/env python3

import sys

def open_file():
    filename = sys.argv[1]
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            for num in line.split():
                numbers.append(float(num))
    return numbers

def sort_file(numbers):
    print(f'The highest mpg is {max(numbers)}')
    print(f'The average is {sum(numbers) / len(numbers)}')

if __name__ == '__main__':
    numbers = open_file()
    sort_file(numbers)
