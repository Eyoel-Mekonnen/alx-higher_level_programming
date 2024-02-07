#!/usr/bin/python3
"""Function that Load, add and save arguments."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        argument_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        argument_list = []

    argument_list.extend(sys.argv[1:])
    save_to_json_file(argument_list, "add_item.json")
