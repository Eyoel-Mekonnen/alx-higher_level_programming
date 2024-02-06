#!/usr/bin/python3
"""Method that will return JSON objects String"""
import json


def to_json_string(my_obj):
    """Defining method to convert to JASON"""
    json_data = json.dumps(my_obj)
    return (json_data)
