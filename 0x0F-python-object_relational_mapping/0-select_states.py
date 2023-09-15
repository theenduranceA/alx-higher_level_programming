#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys import argv

if __name__ == "__main__":

    with MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306) as db:

        db.execute("SELECT * FROM states")
        rows = db.fetchall()
        for row in rows:
            print(row)
