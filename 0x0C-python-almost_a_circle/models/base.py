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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of dict."""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))
