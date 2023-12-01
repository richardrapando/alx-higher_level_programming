#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
