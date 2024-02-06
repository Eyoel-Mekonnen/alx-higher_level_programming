#!/usr/bin/python3
"""Class that inerhits from int"""


class MyInt(int):
    """Defining eq method to reverse its nomral operation"""
    def __eq__(self, y):
        """method to change eq behaviour"""
        if (y is y):
            return (False)
        else:
            return (True)

    def __ne__(self, y):
        """method to override ne"""
        if (self is not y):
            return (True)
