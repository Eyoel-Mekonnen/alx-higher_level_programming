#!/usr/bin/python3
"""Function that will read a file"""


def read_file(filename=""):
    """Defining a method that will read a text file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
