#!/usr/bin/python3
"""Defining a method that Serializes objects attribures"""


def class_to_json(obj):
    """serializes object attributes"""
    return (obj.__dict__)
