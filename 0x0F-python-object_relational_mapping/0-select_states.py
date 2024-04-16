#!/usr/bin/python3


"""
This module provides a utility to connect to MySQL database and retrieve
all entries from the 'states' table, sorting them by
their 'id' in ascending order
"""
import MySQLdb
import sys


def select(username, password_, db_name):
    """function that takes arguments of DB"""
    db = MySQLdb.connect(host="localhost", user=username,
                         password=password_, database=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT states.id, states.name
                   FROM states ORDER BY states.id ASC")
    results = cursor.fetchall()
    for rows in results:
        print(rows)
    if cursor:
        cursor.close()
    if db:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        select(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python script.py <username> <password> <dbname>")
