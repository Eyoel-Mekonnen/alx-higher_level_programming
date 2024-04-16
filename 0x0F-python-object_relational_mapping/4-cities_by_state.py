#!/usr/bin/python3
"""Script that lists all cities from the database"""

import MySQLdb
import sys


def display_cities(username, password_, db_name):
    """Take user, psd, db and city to display"""
    db = MySQLdb.connect(host="localhost", user=username, password=password_,
                         database=db_name, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   INNER JOIN states ON states.id = cities.state_id
                   ORDER BY cities.id ASC""")
    results = cursor.fetchall()
    for rows in results:
        print(rows)
    if cursor:
        cursor.close()
    if db:
        db.close()


if __name__ == "__main__":
    if (len(sys.argv) == 4):
        display_cities(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python script.py <username> <password> <dbname>")
