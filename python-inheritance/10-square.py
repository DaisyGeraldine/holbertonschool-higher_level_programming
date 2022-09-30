#!/usr/bin/python3
"""This module named 10-square.py
   Created on Thursday, September 29, 2022
   @author: Daisy Chipana Lapa
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class Square
    Attributes:
       Nothing
    """
    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)
        super().integer_validator("size", self.__size)

    def area(self):
        return super().area()
