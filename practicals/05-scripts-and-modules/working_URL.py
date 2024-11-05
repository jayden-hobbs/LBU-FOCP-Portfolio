#!/usr/bin/env python3

import requests

if __name__ == '__main__':
    url = input('Enter a URL: ')
    response = requests.get(url)
    print(response.status_code)