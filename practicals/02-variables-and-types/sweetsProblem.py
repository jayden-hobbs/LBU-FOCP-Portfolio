#!/usr/bin/env python3

if __name__ == '__main__':
    numberSweets = int(input('Enter number of sweets: '))
    numberStudents = int(input('Enter number of students: '))
    sweets_per_student = numberSweets//numberStudents
    leftOver = numberStudents % numberSweets
    if leftOver == 1:
        print(f'Each student recieves {sweets_per_student} and there will be 1 sweet left over.')
    else:
        print(f'Each student recieves {sweets_per_student} and there will be {leftOver} sweets left over.')
