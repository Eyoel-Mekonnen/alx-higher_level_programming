#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class created"""

    def __init__(self, width=0, height=0):
        """Creates an instance of the class Rectangle

        Arguments Taken:
        widht (int) = The width of the object
        height (int) = The height of the object
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/sets the width of the object"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/sets the height of the object"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2*(self.width) + 2*(self.height))
