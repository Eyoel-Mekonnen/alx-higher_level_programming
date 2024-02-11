#!/usr/bin/python3
"""Class square To be defined"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square is defined and inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Class square instance is being created."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return (self.__width)

    @size.setter
    def size(self, value):
        """sets the size of square by using its Parent class."""
        self.height = value
        self.width = value

    def __str__(self):
        """Returning the object representation of rectangle"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
