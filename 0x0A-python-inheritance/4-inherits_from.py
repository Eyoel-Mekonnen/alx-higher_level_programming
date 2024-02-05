#!/usr/bin/python3
"""Checks if an object is an instance and also an inheritance"""


def inherits_from(obj, a_class):
    """checking if it is inherited directly
        or indirectly as well as is an instance the
            type checking insures it is inhertited"""
    if (isinstance(obj, a_class) and type(obj) is not a_class):
        return (True)
    else:
        return (False)
