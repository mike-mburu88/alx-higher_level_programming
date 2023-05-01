#!/usr/bin/python3
"""A python script that takes a URL and
email address and sends a POST request to
the passed URL displaying the body of the
response
"""
from sys import argv
from requests import post
if __name__ == "__main__":
    try:
        s = post(argv[1], data={'email: {}'.format(argv[2])})
        print(s.text)
    except Exception as m:
        print(m)
