#!/usr/bin/python3
"""Create a square class that calculates square."""


class Square:
    """Create an instance of the object."""

    def __init__(self, size=0):
        if (type(size) is int and size >= 0):
            self.__size = size
        elif (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        """Returns current Square Area"""
    def area(self):
        return (self.__size * self.__size)
