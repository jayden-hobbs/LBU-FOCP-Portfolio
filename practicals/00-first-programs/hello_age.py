#!/usr/bin/env python3

if __name__ == '__main__':
    name = str(input("Enter your name: "))
    yearNow = int(input('What is the current year? '))
    yearBorn = int(input('Enter your year of birth: '))
    age = yearNow - yearBorn
    print(f'Hello, {name}. You are, {age} years old.')

