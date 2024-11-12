#!/usr/bin/env python3

import math

def find_factors(number):
    factors = []
    for i in range(1, mid_number):
        if number % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    number = int(input('Enter a number: '))
    mid_number = math.ceil(number/2)
    print(f'The factors of {number} are {find_factors(number)}')