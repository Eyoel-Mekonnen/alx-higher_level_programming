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
        return (self.height)

    @size.setter
    def size(self, value):
        """sets the size of square by using its Parent class."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the class square arguments."""
        if (args) and len(args != 0):
            for arg in range(1, len(args)):
                if (arg == 0):
                    if arg is None:
                        self.__init(self.size, self.x, self.y)
                    else:
                        self.id = args[0]
                elif (arg == 1):
                    self.size = args[1]
                elif (arg == 2):
                    self.x = args[2]
                elif (arg == 3):
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                if (key == "id"):
                    if (value is None):
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif (key == "size"):
                    self.size = value
                elif (key == "x"):
                    self.x = value
                elif (key == "y"):
                    self.y = y

    def __str__(self):
        """Returning the object representation of rectangle"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
