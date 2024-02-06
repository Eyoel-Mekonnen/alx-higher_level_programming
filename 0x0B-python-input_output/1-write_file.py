#!/usr/bin/python3
"""A function that writes to a file"""


def write_file(filename="", text=""):
    """Defining the method to write to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
