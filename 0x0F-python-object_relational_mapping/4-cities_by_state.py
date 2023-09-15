#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_0_usa."""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    INNER JOIN states\
                    ON cities.state_id=states.id\
                    ORDER by cities.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
