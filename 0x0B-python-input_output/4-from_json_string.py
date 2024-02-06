#!/usr/bin/python3
"""Function that will convert JSON to string"""
import json


def from_json_string(my_str):
    """Defining json to string method"""
    string_of_json = json.loads(my_str)
    return (string_of_json)
