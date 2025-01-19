#!/usr/bin/env python3

if __name__ == '__main__':
    while True:
        try:
            miles = int(input("Please enter the distance in miles: "))
            if miles >= 0: 
                km = miles * 1.60934
                km_rounded = round(km, 2)
                print(f'{miles} miles is {km_rounded} kilometres')
                break  
            else:
                print("Please enter a value greater than or equal to 0.")  
        except ValueError:
            print("Please enter a valid integer greater than or equal to 0.")  
