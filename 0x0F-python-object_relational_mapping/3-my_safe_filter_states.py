#!/usr/bin/python3

"""script taking arguments and displaying all values in the states table, safe from
MySQL injections """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], port=3306, host="localhost",
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute(
            "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
             (argv[4], ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
