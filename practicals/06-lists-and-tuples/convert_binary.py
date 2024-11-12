#!/usr/bin/env python3

def convert_binary(number):
    binary_number = bin(number)
    return binary_number[2:]

if __name__ == '__main__':
    number = int(input('Enter a number: '))
    print(f'The binary representation of {number} is {convert_binary(number)}')