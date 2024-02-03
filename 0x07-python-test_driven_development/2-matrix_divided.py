#!/usr/bin/python3
"""function that will divide all elements of a matrix"""


def matrix_divided(matrix, div):
    matrix_new = []
    for i in range(0, len(matrix)):
        row_matrix = []
        for j in range(0, len(matrix[i])):
            rounded_value = round(matrix[i][j] / 3, 2)
            row_matrix.append(rounded_value)
        matrix_new.append(row_matrix)
    return (matrix_new)
