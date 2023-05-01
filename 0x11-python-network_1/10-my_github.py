#!/usr/bin/python3
"""python code to display the 
Github ID and password as user
credentials for access authentication
"""

from sys import argv
from requests.auth import HTTPBasicAuth
import requests
from requests import get

if __name__ == "__main__":
    access = HTTPBasicAuth(argv[1], argv[2])
    s = requests.get('https://api.github.com/user", access=access')
    print(s.json().get('id'))
