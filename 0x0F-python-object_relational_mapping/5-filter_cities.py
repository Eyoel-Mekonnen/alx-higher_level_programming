#!/usr/bin/python3
"""Script that takes name of state as argument"""

import MySQLdb
import sys


def display_CS(username, password_, db_name, state_name):
    """Takes usere, psd, db and state_name"""
    db = MySQLdb.connect(host="localhost", password=password_,
                         database=db_name, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities
                   LEFT JOIN states on states.id = cities.state_id
                   WHERE states.name = %s""", (state_name, ))
    results = cursor.fetchall()
    string = ""
    for i in range(0, len(results)):
        string = string + " ".join(results[i])
        if (i != len(results) - 1):
            string = string + ", "
    print(string)
    if cursor:
        cursor.close()
    if db:
        db.close()


if __name__ == "__main__":
    if (len(sys.argv) == 5):
        display_CS(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: python script.py <username> <password> <dbname>")
