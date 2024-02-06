#!/usr/bin/python3
"""Class To convert an object from JSON"""
import json


def load_from_json_file(filename):
    """loading and converting JSON object from a file"""
    with open(filename, 'r') as f:
        json_load = json.load(filename)
        return (json_load)
