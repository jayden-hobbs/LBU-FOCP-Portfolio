#!/usr/bin/env python3

from tabulate import tabulate

def conversion(mph):
    return mph * 1.60934

def main():
    speed = []
    for mph in range(0, 75, 5):
        kmph = conversion(mph)
        speed.append([mph, round(kmph, 2)])
    
    table = tabulate(speed, headers=["Miles per Hour", "Kilometres per Hour"], tablefmt="fancy_grid")
    print(table)

if __name__ == '__main__':
    main()
