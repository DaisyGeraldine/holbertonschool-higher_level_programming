#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module named 1-Square.py
   Created on Wednesday, September 21, 2022
   @author: Daisy Chipana Lapa
"""


class Square:
    """This class is named Square
    Attributes:
       Instantiation with optional size: def __init__(self, size=0):
    """
    def __init__(self, size=0):
        """function constructor __init_
        Args:
             size: is private attribute
        Returns:
             * if size must be an integer, raise a TypeError exception
             * if size is less than 0, raise a ValueError exception
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method named area
           Args:
               self: Variable that refers to the class name
           Returns:
               The current square area
        """
        area_square = self.__size ** 2
        return area_square
