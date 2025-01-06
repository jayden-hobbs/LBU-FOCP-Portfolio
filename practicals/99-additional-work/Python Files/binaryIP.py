#!/usr/bin/env python3

# This code takes an IP address as input and outputs its binary and hexadecimal form

IP = input("Enter an IP address: ")

octets = IP.split('.')

binIP = ''
hexIP = ''

for octet in octets:
    num = int(octet)

    binIP += bin(num)[2:].zfill(8)  
    hexIP += hex(num)[2:].zfill(2)  

print(f"Binary: {binIP}")
print(f"Hexadecimal: {hexIP}")
