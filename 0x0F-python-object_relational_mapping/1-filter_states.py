#!/usr/bin/python3
"""script that list all states with N upper."""

import MySQLdb
import sys


def select_N(username, password_, db_name):
    """accepts username,psd and dbname."""
    db = MySQLdb.connect(host="localhost", user=username, password=password_,
                         database=db_name, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT states.id, states.name FROM states
                   WHERE states.name LIKE BINARY 'N%'
                   ORDER BY states.id ASC""")
    results = cursor.fetchall()
    for rows in results:
        print(rows)
    if cursor:
        cursor.close()
    if db:
        db.close()


if __name__ == "__main__":
    if (len(sys.argv) == 4):
        select_N(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python script.py <username> <password> <dbname>")
