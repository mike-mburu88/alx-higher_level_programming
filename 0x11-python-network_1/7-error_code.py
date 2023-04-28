#!/usr/bin/python3
"""python script that takes a url and
sends a request to the URL and displays
the body of an error code
"""
from sys import argv
import requests


if __name__ == "__main__":
    link = argv[1]
    s = requests.get(link)
    if s.status_code >= 400:
        print("Error code: {}".format(s.status_code))
    else:
        print(s.text)
