#!/usr/bin/python3
"""A python script that takes a URL and
email address and sends a POST request to
the passed URL displaying the body of the
response
"""
from sys import argv
import requests
if __name__ == "__main__":
    link = argv[1]
    mvalue = ("email: {}".format(argv[2]))
    s = requests.post(link, mvalue)
    print(s.text)
