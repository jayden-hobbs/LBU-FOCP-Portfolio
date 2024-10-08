#!/usr/bin/env python3

if __name__ == '__main__':
    password_1 = str(input('Enter your password: '))
    password_2 = str(input('Confirm your password: '))
    if password_1 == password_2:
        print('Password Confirmed')
        password_Final = password_2
    else:
        print('Passwords do not match')

