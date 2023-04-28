#!/usr/bin/python3
"""performs a fetch operation on
https://intranet.hbtn.io/status"""

import urllib.parse
import urllib.request

if __name__ == "__main__":
    access = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(access) as response:
        page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('UTF-8')))
