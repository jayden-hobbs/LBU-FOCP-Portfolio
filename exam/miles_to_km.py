#!/usr/bin/env python3

if __name__ == '__main__':
    while True:
        try:
            miles = int(input("Please enter the distance in miles: "))
            if miles < 0:
                km = miles * 1.60934
                return miles
                return km
                break
        except ValueError:
            print("Please enter an integer greater than or equal to 0")

    print(f'{miles} miles is {km} kilometres')


       


