#!/usr/bin/env python3

import requests

if __name__ == '__main__':
    url = str(input("Enter a URL: "))
    status_codes = {}
    with open('C:/Users/Seagu/OneDrive - Leeds Beckett University/Computer Programming/Visual Studio Code/programming-portfolio-jayden-hobbs/practicals/05-scripts-and-modules/status_codes.txt', 'r') as file:
        for line in file:
            parts = line.split().split(' ', 1)
            if len == 2:
                code, message = parts
                status_codes[int(code)] = message

    response = requests.get(url)
    status_message = status_codes.get(response.status_code, f'Unknown status code: {response.status_code}')
    print(f'The status code is: {response.status_code} - {status_message}')