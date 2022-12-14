#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module named 0-rectangle.py
   Created on Monday, September 26, 2022
   @author: Daisy Chipana Lapa
"""


class Rectangle:
    """This class is named rectangle
    Attributes:
       Empty class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif not value >= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif not value >= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
