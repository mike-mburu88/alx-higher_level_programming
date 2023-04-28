#!usr/bin/python3
"""python code to retrieve the 10 most recent Github commits as specfied on command line
"""

from requests import get
from sys import argv

link = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])

try:
    s = get(link)
    t = s.json()
    for commit in t[:10]:
        print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit')
                                  .get('author')
                                  .get('name')))
except IndexError as x:
    print(x)
