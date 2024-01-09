#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    for i in range(0, row):
        for j in range(0, len(matrix[i])):
            if (j + 1 != len(matrix[i])):
                print("{:d} ".format(matrix[i][j]), end='')
            else:
                print("{:d}".format(matrix[i][j]), end='')
        print("")
