#!/usr/bin/python3
"""Defining a class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiation of class student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """defining to json method"""
        if (attrs is None):
            return (self.__dict__)
        attribute = {}
        for attr in attrs:
            if (isinstance(attr, str)):
                value = getattr(self, attr, None)
                if (value is not None):
                    attribute[attr] = value
        return (attribute)
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replace all attributes of student instance"""
        for key, value in json.items():
            setattr(self, key, value)
