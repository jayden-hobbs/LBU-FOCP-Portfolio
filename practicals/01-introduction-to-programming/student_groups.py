#!/usr/bin/env python3

if __name__ == '__main__':
    groupSize = int(input('Enter the size of the group: '))
    labSize = int(input('Enter the size of the lab: '))

    fullGroups = groupSize // labSize
    left_over = groupSize % labSize
    print(f'You can have {fullGroups} full groups and {left_over} left over.')
