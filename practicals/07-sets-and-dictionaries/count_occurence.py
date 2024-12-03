#!/usr/bin/env python3

from collections import Counter

def most_common_letters(message):
    message = message.lower()
    return Counter(message).most_common(3)

message = str(input("Enter a message: "))
print(most_common_letters(message))
