#!/usr/bin/python3
"""A code that takes the state name as an argument
and list the cities of the state
takes 3 arguments:
username
password
database name
Connects to a default localhost and port 3306
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    Query1 = " ".join([
        "SELECT cities.name FROM cities",
        "INNER JOIN states ON states.id = cities.state_id",
        "WHERE states.name LIKE BINARY '{}'",
        "ORDER BY cities.id",
        ]).format(argv[4])
    c.execute(Query1)
    res = c.fetchall()
    strRes = ', '.join([x[0] for x in res])
    print(strRes)
    c.close()
    db.close()
