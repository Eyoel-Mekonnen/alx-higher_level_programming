#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        row_matrix = []
        for j in range(len(matrix[i])):
            row_matrix.append(matrix[i][j] ** 2)
        new_matrix.append(row_matrix)
    return new_matrix
