#!/usr/bin/python3
"""The script takes in three arguments from the database:
username
password 
name of the database 
and connects to the local host and port no. 3306
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM 'states'")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close
    db.close
