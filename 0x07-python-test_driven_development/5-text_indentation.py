#!/usr/bin/python3
"""Prints a text with two new lines"""


def text_indentation(text):
    """Text indentation method
        Args: text
        Raise: text must be a string
        Return: prints text with two lines after characters ., ? and :
    """
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        if (text[i] != "." and text[i] != "?" and text[i] != ":"):
            print("{}".format(text[i]), end="")
        elif (text[i] == "." or text[i] == "?" or text[i] == ":"):
            print("{}".format(text[i]), end="")
            print("\n")
            if (text[i + 1] == '\t' or text[i+1] == ' ' or text[i] == '\n'):
                i = i + 1
        i = i + 1
