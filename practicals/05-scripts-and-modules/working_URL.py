#!/usr/bin/env python3

import requests

if __name__ == '__main__':

    try:
        url = input('Enter a URL: ')
        response = requests.get(url)
        if response.status_code == 200:
            print('Success!')
        elif response.status_code == 404:
            print('Not Found.')
        else:
            print(f'Something went wrong. The response is {response.status_code}')
    except requests.exceptions.MissingSchema or requests.exceptions.InvalidSchema or requests.exceptions.InvalidURL:
        print('Invalid URL')