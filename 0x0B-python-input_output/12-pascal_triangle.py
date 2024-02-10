#!/usr/bin/python3
"""Function that operates on pascals traingle"""


def pascal_triangle(n):
    """Function for pascal triangle made"""
    list_1 = []
    if (n <= 0):
        return (list_1)
    for i in range(0, n):
        list_2 = [0] * (i + 1)
        for j in range(0, i + 1):
            if (i == j or j == 0):
                list_2[j] = 1
            else:
                list_2[j] = list_1[i-1][j-1] + list_1[i-1][j]
        list_1.append(list_2)
    return (list_1)
