#!/usr/bin/env python3

if __name__ == '__main__':
    password_set = False
    while password_set == False:
        password_1 = str(input('Enter your password: '))
        password_2 = str(input('Confirm your password: '))
        if password_1 == password_2:
            password_Final = password_2
            if 8<= len(password_Final) <=12:
                password_set = True
            else:
                print("Password must be between 8 and 12")
        else:
            print('Passwords do not match')


    print("Password Confirmed")



