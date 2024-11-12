#!/usr/bin/env python3
    
if __name__ == '__main__':
    text = input("Enter a text: ")
    encrypted_text = text.replace(" ", "")[::-1]
    print(f"Encrypted text: {encrypted_text}")
