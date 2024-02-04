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
    for i in range(0, len(text)):
        if (i > 0):
            if (text[i - 1] == "." or text[i - 1] == "?" or text[i - 1] == ":"):
                print("")
                print("")
            else:
                if (text[i]) == " "):
                    continue
                print("{}".format(text[i]), end="")
        elif (text[i] == " "):
            continue
        else:
            print("{}".format(text[i]), end="")
