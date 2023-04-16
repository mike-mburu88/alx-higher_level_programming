#!/usr/bin/python3
"""A script that displays all state values as per the metadata
takes 4 arguments:
    username
    password 
    name 
    matching name
connects to default localhost and port 3306
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM 'states' WHERE BINARY 'name' = '{}'".format(sys.argv[4]))
[print(state) for state in c.fetchall()]
