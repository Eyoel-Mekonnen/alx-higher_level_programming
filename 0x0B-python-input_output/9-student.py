#!/usr/bin/python3
"""Studnet class defination"""


class Student:
    """Class student instiation."""
    def __init__(self, first_name, last_name, age):
        """instance of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """give dictionary reperesentaion of self"""
        return (self.__dict__)
