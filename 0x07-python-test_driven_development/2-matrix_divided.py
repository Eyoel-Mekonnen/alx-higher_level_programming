#!/usr/bin/python3
"""function that will divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Divide all elements of a matrix.

    Args:
        matrix -it takes a list of list that contain float or integers
        div - a number to divide each element of the list
    Raises:
        TypeError: if matrix is not a list
        TypeError: if matrix is not a list of list
        TypeError: if row of the matirx is not consitent
        TypeError: if memebers of row are not integers or floats
        ZeroDivisionError: if the div argument is zero
    Returns:
        A new matrix that divides each element by div
    """

    matrix_new = []

    length = len(matrix[0])
    if not (isinstance(matrix, list)):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")
    for i in matrix:
        if not (isinstance(i, list)):
            raise TypeError("matrix must be a matrix (list of lists) of"
                            "integers/floats")
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for member in i:
            if not (isinstance(member, (int, float))):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    if not (isinstance(div, (float, int))):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    for i in range(0, len(matrix)):
        row_matrix = []
        for j in range(0, len(matrix[i])):
            rounded_value = round(matrix[i][j] / div, 2)
            row_matrix.append(rounded_value)
        matrix_new.append(row_matrix)
    return (matrix_new)
