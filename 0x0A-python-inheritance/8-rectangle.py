#!/usr/bin/python3
from 7-base_geometry import BaseGeometry
"""Class Rectangle """


def Rectangle(BaseGeometry):
    """instantiaiton will happen"""
    def __init__(self, width, height):
        integer_validator(self, width)
        self.__width = width
        integer_validator(self, height)
        self.__height = height
