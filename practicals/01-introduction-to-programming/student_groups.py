#!/usr/bin/env python3

if __name__ == '__main__':
    group_size = int(input('Enter the size of the group: '))
    lab_size = int(input('Enter the size of the lab: '))

    full_groups = group_size // lab_size
    left_over = group_size % lab_size
    print(f'You can have {full_groups} full groups and {left_over} left over.')
