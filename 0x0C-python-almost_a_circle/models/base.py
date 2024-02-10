#!/usr/bin/python3
""" Class Base about to be created"""


class Base:
    """Base class defined."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Base class initialized."""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
