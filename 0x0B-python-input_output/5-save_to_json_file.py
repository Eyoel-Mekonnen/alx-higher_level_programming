#!/usr/bin/python3
"""Defining a Function to write to text using """
import json


def save_to_json_file(my_obj, filename):
    """Defines method to save json to file name"""
    json_object = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        wirte_data = f.write(json_object)
