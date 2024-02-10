#!/usr/bin/python3
"""Class Base."""
from models.base import Base


class Rectangle(Base):
    """Class rectangle that inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instatniation of Rectangel class
        Args: width
            : height
            : x
            : y
            : id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the value of self.__width private attribute."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the value self.__width but after checking its value."""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """returns the value of self.__height private attribute."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the value of self.__height but after checking its value."""
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """returns the value of self.__x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets the value of self.__x but after checking its value."""
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """returns the value of self.__y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets the value of self.__y but after checking its value."""
        if (y < 0):
            raise ValueError("y must b >= 0")
        self.__y = y
