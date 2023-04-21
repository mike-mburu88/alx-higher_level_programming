#!/usr/bin/python3
"""A code to list all cities within a database that have been joined
takes 3 arguments:
username
password
database name
Connects to a default local host and port 3306
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    [print(city) for city in c.fetchall()]
