#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary_keys = a_dictionary.keys()
    for keys in sorted(a_dictionary_keys):
        print("{}: {}".format(keys, a_dictionary.get(keys)))
