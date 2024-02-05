#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Class Rectangle """


def Rectangle(BaseGeometry):
    """instantiaiton will happen"""

    def __init__(self, width, height):
        integer_validator("width", width)
        self.__width = width
        integer_validator("height", height)
        self.__height = height
