#!/usr/bin/python3
"""This module named 8-rectangle.py
   Created on Thursday, September 29, 2022
   @author: Daisy Chipana Lapa
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class Rectangle
    Attributes:
       Nothing
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
