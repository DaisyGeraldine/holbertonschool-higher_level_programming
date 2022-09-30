#!/usr/bin/python3
"""This module named 7-base_geometry.py
   Created on Thursday, September 29, 2022
   @author: Daisy Chipana Lapa
"""


class BaseGeometry:
    """This class BaseGeometry
    Attributes:
       Nothing
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value < 0 or value == 0:
            raise ValueError(name + " must be greater than 0")
