#!/usr/bin/env python3

if __name__ == '__main__':
    password1 = str(input('Enter your password: '))
    password2 = str(input('Confirm your password: '))
    if password1 == password2:
        print('Password Confirmed')
        passwordFinal = password2
    else:
        print('Passwords do not match')

