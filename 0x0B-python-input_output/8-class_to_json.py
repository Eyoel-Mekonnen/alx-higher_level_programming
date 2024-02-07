#!/usr/bin/python3
"""Defining a method that Serializes object attribute"""


def class_to_json(obj):
    """serializes object attribute"""
    return (obj.__dict__)
