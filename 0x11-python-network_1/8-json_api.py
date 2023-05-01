#!/usr/bin/python3
"""script that takes in a letter
and sends a POST request to a website
address with the specified port
"""
from sys import argv
from requests import get, post

if __name__ == '__main__':
    try:
        if len(argv) < 2:
            l = ""
        else:
            l = argv[1]
        s = post("http://0.0.0.0:5000/search_user", data ={'q': l})
        t = s.json()
        if not t:
            print("No Result")
        else:
            print("[{}] {}".format(t.get('id), t.get(name')))
    except ValueError:
        print("Not a valid JSON")
        
