#!/usr/bin/env python3

import random
import string

def encrypt_message(message):
    interval = random.randint(1, 20)
    message_index = 0
    encrypted_message = []

    for i in range(100):
        if i % interval == 0:
            print(message[message_index], end="")
            message_index += 1
            if message_index == len(message):
                break
        else:
            encrypted_message.append(random.choice(string.ascii_letters))

    encrypted_message = " ".join(encrypted_message)
    return encrypted_message, interval

if __name__ == '__main__':
    message = input("Enter a message: ")
    encrypted_message, interval = encrypt_message(message)
    print(f"\nEncrypted message: {encrypted_message}")
    print(f"Interval: {interval}")