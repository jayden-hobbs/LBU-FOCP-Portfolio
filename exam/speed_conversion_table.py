#!/usr/bin/env python3

from tabulate import tabulate

if __name__ == '__main__':
    speed = []
    for mph in range(0, 75, 5):
        kmph = mph * 1.60934
        speed.append([mph, round(kmph, 2)])
    
    table = tabulate(speed, headers=["Miles per Hour", "Kilometres per Hour"], tablefmt="fancy_grid")
    print(table) 