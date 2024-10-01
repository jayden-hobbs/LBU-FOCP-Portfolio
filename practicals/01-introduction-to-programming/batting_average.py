#!/usr/bin/env python3

if __name__ == '__main__':
    matches = int(input('Enter the number of matches played: '))
    batted_times = int(input('Enter the number of times batted: '))
    not_out = int(input('Enter the number of times not out: '))
    runs_scored = int(input('Enter the number of runs scored: '))

    completed_innings = batted_times - not_out
    batting_average = runs_scored // completed_innings
    print(f'Geoffrey had a batting average of {batting_average}')
