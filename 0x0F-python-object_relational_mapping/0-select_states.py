#!/usr/bin/python3
"""The script takes in three arguments from the database:
username
password 
name of the database 
and connects to the local host and port no. 3306
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    [print(state) for state in c.fetchall()]
