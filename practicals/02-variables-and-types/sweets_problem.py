#!/usr/bin/env python3

if __name__ == '__main__':
    number_sweets = int(input('Enter number of sweets: '))
    number_students = int(input('Enter number of students: '))
    sweets_per_student = number_sweets//number_students
    left_over = number_students % number_sweets
    if left_over == 1:
        print(f'Each student receives {sweets_per_student} and there will be 1 sweet left over.')
    else:
        print(f'Each student receives {sweets_per_student} and there will be {left_over} sweets left over.')
