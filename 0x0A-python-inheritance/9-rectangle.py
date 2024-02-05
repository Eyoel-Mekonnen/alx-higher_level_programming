#!/usr/bin/python3
"""Class Rectangle that inherits from Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class create"""

    def __init__(self, width, height):
        """Instance of rectangle activated"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method that finds area"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns Rectangle discritpion"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
