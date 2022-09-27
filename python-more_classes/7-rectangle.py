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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Public instance method named area
           Args:
               self: Variable that refers to the class name
           Returns:
               The current Rectangle area
        """
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """Public instance method named perimeter
           Args:
               self: Variable that refers to the class name
           Returns:
               The current Rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = self.__height * 2 + self.__width * 2
        return perimeter

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__width == 0:
            print(string, end="")
        else:
            for i in range(self.__height):
                string += str(self.print_symbol) * self.__width
                if i != self.__height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
