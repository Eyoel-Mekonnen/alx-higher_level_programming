#!/usr/bin/python3
"""scripts takes 4 arguments and display values"""

import MySQLdb
import sys


def display(username, password_, db_name, state):
    """searches for the required state"""
    db = MySQLdb.connect(host="localhost", user=username,
                         database=db_name, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT states.id, states.name FROM
                   states WHERE states.name = '{}'""".format(state))
    results = cursor.fetchall()
    for rows in results:
        print(rows)
    if cursor:
        cursor.close()
    if db:
        db.close()


if __name__ == "__main__":
    if (len(sys.argv) == 5):
        display(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: python script.py <username> <password> <dbname>")
