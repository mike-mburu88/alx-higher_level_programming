#!/usr/bin/python3
"""a python script that takes a URL and sends
a request and displays the value X-Request-Id
found in the header response
"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    link = argv[1]
    access = urllib.request.Request(link)
    with urllib.request.urlopen(access) as response:
        print(dict(response.headers).get("X-Request-Id"))
