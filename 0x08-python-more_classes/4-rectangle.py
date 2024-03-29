#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class Created"""

    def __init__(self, width=0, height=0):
        """Creates an instance of the class Rectangle

        Arguments Taken:
        Width (int) = The width of the object
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
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2*(self.__width) + 2*(self.__height))

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ("")
        string = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                string = string + "#"
            if i < self.__height - 1:
                string = string + "\n"
        return (string)

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")
