#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    if sys.platform == 'darwin':
        print('You are using macOS')
    if sys.platform == 'win32' or 'win64':
        print('You are using Windows')
    if sys.platform == 'linux':
        print('You are using Linux')
     
                
