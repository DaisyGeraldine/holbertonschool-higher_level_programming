#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module named rectangle.py
   Created on Wednesday, October 05, 2022
   @author: Daisy Chipana Lapa
"""


from models.base import Base


class Rectangle(Base):
    """
       This class is named Rectangule
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Public method named area
           Args:
               self: Variable referring to the same instance
           Returns:
               The area value of the Rectangle instance
        """
        area = self.__height * self.__width
        return area

    def display(self):
        """ Public method named display
           Args:
               self: Variable referring to the same instance
           Returns:
               Prints in stdout the Rectangle instance with the character #
        """
        for c_y in range(self.__y):
            print()

        for row in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="")
            if row < self.__height - 1:
                print()
        print()

    def update(self, *args, **kwargs):
        """ Public method named update
           Args:
               args: Variable referring to the same instancthat
                     assigns an argument to each attributee
                * 1st argument should be the id attribute
                * 2nd argument should be the width attribute
                * 3rd argument should be the height attribute
                * 4th argument should be the x attribute
                * 5th argument should be the y attribute
              kwargs: must be skipped if *args exists and is not empty
        """
        for num in range(len(args)):
            setattr(self, 'id' if num == 0
                    else 'width' if num == 1
                    else 'height' if num == 2
                    else 'x' if num == 3
                    else 'y', args[num])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        string1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        string2 = f" - {self.__width}/{self.__height}"
        return string1 + string2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def to_dictionary(self):
        """ Public method named to_dictionary
           Args:
               self: Variable referring to the same instance
           Returns:
               that returns the dictionary representation of a Rectangle
        """
        dic = {"x": self.x, "y": self.y, "id": self.id,
               "height": self.height, "width": self.width}
        return dic
