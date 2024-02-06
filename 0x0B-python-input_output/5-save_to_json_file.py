#!/usr/bin/python3
"""Defining a Function to write to text using """
import json


def save_to_json_file(my_obj, filename):
    """Defines method to save json to file name"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
