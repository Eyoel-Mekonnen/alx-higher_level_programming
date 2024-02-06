#!/usr/bin/python3
"""Method that will return JSON objects String"""


def to_jason_string(my_obj):
    """Defining method to convert to JASON"""
    jason_data = json.dumps(my_obj)
    return (jason_data)
