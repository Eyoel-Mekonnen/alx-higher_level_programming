#!/usr/bin/python3
"""Method that will append"""


def append_write(filename="", text=""):
    """Defining an append method"""
    with open(filename, 'a', encoding="utf-8") as f:
        append_data = f.write(text)
    return (append_data)
