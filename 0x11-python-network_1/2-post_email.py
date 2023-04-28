#!/usr/bin/python3
"""A python script to send a POST verb message to 
a url and displays the body of the response"""

from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    link = argv[1]
    mail = {"email": argv[2]}
    data = urllib.parse.urlencode(mail).encode("ascii")

    access = urllib.request.Request(link, data)
    with urllib.request.urlopen(access) as response:
        print(response.read().decode('utf-8'))
            
    
