#!/usr/bin/env python3

import requests

if __name__ == '__main__':
    url = str(input("Enter a URL: "))
    status_codes = {}
    with open('status_codes.txt', 'r') as in_file:
        for line in in_file:
            code, message = line.split(' ', 1)
            status_codes[int(code)] = message.strip()

    try:
        response = requests.get(url)
    except Exception as e:
        print('Error connecting to web host.')
    finally:
        status_message = status_codes.get(response.status_code, f'Unknown status code: {response.status_code}')
        print(f'The status code is: {response.status_code} - {status_message}')