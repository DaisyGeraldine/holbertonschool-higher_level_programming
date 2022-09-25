#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module 2-matrix_divided.py
   Created on Sunday, September 25, 2022
   @author: Daisy Chipana Lapa
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.
        Args:
             matrix: must be a list of lists of integers or floats
             div:  can’t be equal to 0
        Returns:
             Returns a new matrix
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    for row in matrix:
        first_row = len(matrix[0])
        if len(row) != first_row:
            raise TypeError("Each row of the matrix must have the same size")
        for value in row:
            if not isinstance(value, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    r = list(map(lambda lista:
                 list(map(lambda x: round(x / div, 2), lista)), matrix))
    return r
