#!/usr/bin/python3
""""python script to take a URL,
send a request to the URL and
return the body of the response in utf-8
"""
from sys import argv
import urllib.request
import urllib.error

if __name__ == "__main__":
    link = argv[1]
    access = urllib.request.Request(link)
    try:
        with urllib.request.urlopen(access)as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as r:
        print('Error code: {}'.format(r.code))
