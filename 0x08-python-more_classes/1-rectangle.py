#!/usr/bin/python3
"""Class Rectangle Defined"""


class Rectangle:
    """Rectangle """

    def __init__(self, width=0, height=0):
        """Creates an instance of the class Rectangle.

        Arguments Taken:
            width (int): The widht of the object
            height (int): The height of the object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/sets the width of the object"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width msut be >= 0")
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
