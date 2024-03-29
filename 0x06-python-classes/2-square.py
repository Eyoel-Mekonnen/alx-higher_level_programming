#!/usr/bin/python3
"""Create a square that defines square."""


class Square:
    """creating an instance."""

    def __init__(self, size=0):
        """Assigning private size attribute."""

        if (type(size) is int and size >= 0):
            self.__size = size
        elif (type(size)) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
