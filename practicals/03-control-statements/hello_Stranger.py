#!/usr/bin/env python3

if __name__ == '__main__':
    name = str(input('What is your name? '))
    lenName = len(name)
    if lenName == 0:
        print("Hello Stranger!")
    else:
        print(f'Hello {name}! ')
