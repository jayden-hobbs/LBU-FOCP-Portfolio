#!/usr/bin/env python3

if __name__ == '__main__':
    name = str(input('What is your name? '))
    len_name = len(name)
    if len_name == 0:
        print("Hello Stranger!")
    else:
        print(f'Hello {name}! ')
