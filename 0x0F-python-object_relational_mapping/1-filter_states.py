#!/usr/bin/python3
"""lists all the states that have their names starting with N from a databases
takes 3 arguments:
username
password
database name
connects to a default localhost and port 3306
"""

from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host=localhost, user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
