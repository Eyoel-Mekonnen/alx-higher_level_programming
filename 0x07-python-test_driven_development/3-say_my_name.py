#!/usr/bin/python3
""" Define a method that prints name"""


def say_my_name(first_name, last_name=""):

    """defining say_my_name.
        Args:
            first_name: string
            last_name: string and default value is ""
        Returns:
            My name is <first name> <last name>
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
