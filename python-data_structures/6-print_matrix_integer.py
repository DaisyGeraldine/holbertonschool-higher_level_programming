#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j + 1) != len(matrix[i]):
                print("{} ".format(matrix[i][j]), end="")
                continue
            print("{}".format(matrix[i][j]))
