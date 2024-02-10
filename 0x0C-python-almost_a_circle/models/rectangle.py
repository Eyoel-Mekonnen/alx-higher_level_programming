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
