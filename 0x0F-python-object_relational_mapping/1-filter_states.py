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
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")
    result = c.fetchall()
    for row in result:
        print(row)

    c.close()
    db.close()
