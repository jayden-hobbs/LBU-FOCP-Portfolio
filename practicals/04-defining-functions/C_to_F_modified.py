#!/usr/bin/env python3

temperature = str(input("""Please enter the temperature and units(e.g. 32C or 73F)"""))
if "C" in temperature:
    temp = int(temperature[:2])
    print(f"The temperature is, {temp* 1.8 + 32}F")
    if "F" in temperature:    temp = int(temperature[:2])
    print(f"The temperature is, {(temp-32)/1.8}C")