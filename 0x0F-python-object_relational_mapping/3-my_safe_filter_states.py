#!/usr/bin/python3
""" Accept use input as single data."""


import MySQLdb
import sys


def display_param(username, password_, db_name, parameter):
    """Take argument and display values in the database."""
    db = MySQLdb.connect(host="localhost", user=username,
                         password=password_, database=db_name, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT states.id, states.name
                   FROM states WHERE states.name = %s""",
                   (parameter, ))
    results = cursor.fetchall()
    for rows in results:
        print(rows)
    if cursor:
        cursor.close()
    if db:
        db.close()


if __name__ == "__main__":
    if (len(sys.argv) == 5):
        display_param(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: python script.py <username> <password> <dbname>")
