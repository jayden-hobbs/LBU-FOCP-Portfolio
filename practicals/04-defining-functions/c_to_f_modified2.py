#!/usr/bin/env python3

choice = int(input("""Would you like to convert fromC.Degrees to fahrenheitF.Fahrenheit to degrees?"""))
if choice == 'C':
    temp_C = int(input("What is the temp in Degrees?"))
    print(f"The temperature in fahrenheit is {temp_C *1.8 +32}")
elif choice == 'F':
    temp_F = int(input("What is the temp in fahrenheit?"))
    print (f"The temperature in degrees is {(temp_F - 32) / 1.8}")
else:
    print("please enter a correct option!")