#!/usr/bin/python3
"""A code that takes the state name as an argument and list the cities of the state
takes 3 arguments:
username
password
database name
Connects to a default localhost and port 3306
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connection(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM 'cities' INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY citie.id ASC")
print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
