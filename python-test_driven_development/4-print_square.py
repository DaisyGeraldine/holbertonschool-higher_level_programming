#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module 4-print_square.py
   Created on Sunday, September 25, 2022
   @author: Daisy Chipana Lapa
"""


def print_square(size):
    """function that prints a square with the character #.
        Args:
             size: is the size length of the square
        Returns:
             prints a square with the character #
    """
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
    else:
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
