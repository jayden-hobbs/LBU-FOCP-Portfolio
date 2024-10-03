#!/usr/bin/env python3

if __name__ == '__main__':
    totalStudents = int(input("Enter total number of students: "))
    groupSize = int(input("Enter group size: "))
    fullGroups = int(totalStudents//groupSize)
    leftOver = int(totalStudents % groupSize)
    if leftOver == 1:
        print(f'There will be {fullGroups} full groups and 1 student left over.')
    else:
        print(f'There will be {fullGroups} full groups and {leftOver} students left over.')