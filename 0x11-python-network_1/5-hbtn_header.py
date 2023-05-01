#!/usr/bin/python3
"""A python script that takes the URL,
then sends the request to display the value
inside a variable in the response header
"""

from sys import argv
import requests

if __name__ == "__main__":
    link = argv[1]
    output = requests.get(link)
    print(output.headers.get("X-Request-Id"))
