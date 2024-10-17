#!/usr/bin/env python3

choice = str(input("""Would you like to convert from C or F? """))
if choice == 'C' or 'c':
    temp_C = int(input("What is the temp in Degrees? "))
    print(f"The temperature in fahrenheit is {temp_C *1.8 +32}")
elif choice == 'F' or 'f':
    temp_F = int(input("What is the temp in fahrenheit? "))
    print (f"The temperature in degrees is {(temp_F - 32) / 1.8}")
else:
    print("please enter a correct option!")