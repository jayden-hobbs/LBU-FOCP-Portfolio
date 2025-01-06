#!/usr/bin/env python3

message = input("Enter message: ")
character = input("Which character should I search for? ")
count = 0

i = 0
while i <= len(message) - 1:
     if message[i] == character:
          count += 1
     i = i + 1
     
print(character + " appears " + str(count) + " times in the text.")