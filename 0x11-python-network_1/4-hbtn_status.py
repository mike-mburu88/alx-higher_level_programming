#!/usr/bin/python3
"""A python script that fetches
https://alx-intranet.hbtn.io/status
and returns the body of the response
"""
import requests

if __name__ == "__main__":
    access = get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(access.text)))
    print("\t- content: {}".format(access.text))
    
