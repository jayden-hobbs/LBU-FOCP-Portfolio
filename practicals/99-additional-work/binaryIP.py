#!/usr/bin/env python3

#! This code takes in an IP address as an input and outputs in binary and hexadecimal form

IP = input("Enter an IP address: ")
binIP = bin(int(IP))[2:]
hexIP = hex(int(IP))[2:]

print(f"Binary: {binIP} \nHexadecimal: {hexIP}")
