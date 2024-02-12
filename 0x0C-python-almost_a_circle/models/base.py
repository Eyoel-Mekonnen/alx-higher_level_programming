#!/usr/bin/python3
""" Class Base about to be created"""
import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string reprsentation to file"""
        class_file = cls.__name__ + ".json"
        with open(class_file, "w", encoding="utf-8") as f:
            if list_objs is None:
                list_objs = "[]"
                f.write(list_objs)
            else:
                list_dict = []
                for j in list_objs:
                    list_dict.append(j.to_dictionary())
                json_file = Base.to_json_string(list_dict)
                f.write(json_file)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of json string representation."""
        if (json_string is None or json_string == "[]"):
            list_ = []
            return (list_)
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """create a dictionary"""
        if 'size' in dictionary:
            dummy_instance = cls(1)
        elif 'width' in dictionary and 'height' in dictionary:
            dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """Loads from file."""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                json_file = Base.from_json_string(f.read())
                list_of_instances = []
                for instance in json_file:
                    list_of_instances.append(cls.create(**instance))
                return list_of_instances
        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file."""
        csv_file = cls.__name__ + ".csv"
        if (cls.__name__ == "Rectangle"):
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']
        with open(csv_file, "w", newline="") as f:
            encoder = csv.DictWriter(f, fieldnames=fieldnames)
        for lists in list_objs:
            encoder.writerow(lists)

