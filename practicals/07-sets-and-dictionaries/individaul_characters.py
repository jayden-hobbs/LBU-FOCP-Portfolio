#!/usr/bin/env python3


if __name__ == "__main__":


    def unique_letters(input_string):
        unique_chars = set(input_string)
        for char in unique_chars:
            print(char)

    user_input = str(input("Enter a string: "))
    unique_letters(user_input)
