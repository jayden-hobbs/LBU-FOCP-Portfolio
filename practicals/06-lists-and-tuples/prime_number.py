# #!/usr/bin/env python3

from sympy import isprime

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    if isprime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
