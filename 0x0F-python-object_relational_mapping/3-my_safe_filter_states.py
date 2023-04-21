#!/usr/bin/python3
"""tests an SQL injection placed on the database and displays state
Code takes 4 arguments:
username
password
name of the databae
matching name
Connects to a default localhost and port 3306
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    parameter = (argv[4], )
    c.execute("SELECT * FROM states WHERE name = %s\
            ORDER BY states.id ASC", parameter)
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
