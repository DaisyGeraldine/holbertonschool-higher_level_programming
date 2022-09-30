#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""This module named 8-rectangle.py
   Created on Thursday, September 29, 2022
   @author: Daisy Chipana Lapa
"""


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
