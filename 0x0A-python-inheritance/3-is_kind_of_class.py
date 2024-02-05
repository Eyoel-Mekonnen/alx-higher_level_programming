#!/usr/bin/python3
"""Check wether an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance"""
    if (isinstance(obj, a_class)):
        return (True)
    else:
        return (False)
