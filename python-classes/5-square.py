#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module named 1-Square.py
   Created on Wednesday, September 22, 2022
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
             size: is first parameter
        Returns:
             nothing
        """
        self.size = size

    @property
    def size(self):
        """Property size to retrieve it- it's getter
           Args:
               self: Variable that refers to the class name
           Returns:
               The size validated
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter size to set it - it's setter
        Args:
             value: is first parameter to validate
        Returns:
             * if size must be an integer, raise a TypeError exception
             * if size is less than 0, raise a ValueError exception
        Otherwise define the value validated
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method named area
           Args:
               self: Variable that refers to the class name
           Returns:
               The current square area
        """
        area_square = self.__size ** 2
        return area_square

    def my_print(self):
        """Public instance method named my_print
           Args:
               self: Variable that refers to the class name
           Returns:
               * That prints in stdout the square with the character #
               * if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('{}'.format("#" * self.__size))
