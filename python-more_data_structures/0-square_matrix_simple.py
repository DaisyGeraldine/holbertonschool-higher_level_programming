#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_matrix = matrix[:]
    for i in range(len(matrix)):
        new_matrix[i] = matrix[i][:]
        for j in range(len(matrix[i])):
            square = matrix[i][j] ** 2
            new_matrix[i][j] = square
    return new_matrix
