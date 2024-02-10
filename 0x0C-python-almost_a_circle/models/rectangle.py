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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        self.__width = value

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
        self.__height = value

    @property
    def x(self):
        """returns the value of self.__x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets the value of self.__x but after checking its value."""
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the value of self.__y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets the value of self.__y but after checking its value."""
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Rectangle of area calculated"""
        return (self.__width * self.__height)

    def display(self):
        """displays the rectangle"""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Returns descritpion of the instance of the class"""
        return ("[Rectangle] " + "(" + str(self.id) + ")"
                " " + str(self.__x) + "/" + str(self.__y) + " - "
                + str(self.__width) + "/" + str(self.__height))
