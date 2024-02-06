#!/usr/bin/python3
import json
"""Method that will return JSON objects String"""


def to_json_string(my_obj):
    """Defining method to convert to JASON"""
    jason_data = json.dumps(my_obj)
    return (jason_data)
