#!/usr/bin/python3
"""Method that pring #"""


def print_square(size):
    """print square.
        Args: size
        Raise: size is not an integer
               size must not be less than 0
               size is float and less than 0
        Return:
            prints the #
    """
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0"):
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
