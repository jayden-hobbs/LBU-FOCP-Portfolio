#!/usr/bin/env python3

def get_name():
    input_name = str(input("Enter your name: "))
    print(f'{input_name.capitalize()}')

if __name__ == '__main__':
    get_name()