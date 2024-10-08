#!/usr/bin/env python3

if __name__ == '__main__':
    total_students = int(input("Enter total number of students: "))
    group_size = int(input("Enter group size: "))
    full_groups = int(total_students//group_size)
    left_over = int(total_students % group_size)
    if left_over == 1:
        print(f'There will be {full_groups} full groups and 1 student left over.')
    else:
        print(f'There will be {full_groups} full groups and {left_over} students left over.')