#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module named square.py
   Created on Thursday, October 06, 2022
   @author: Daisy Chipana Lapa
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
       This class is named Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        string = f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
        return string

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Public method named update
           Args:
               args: is the list of arguments - no-keyworded arguments
                * 1st argument should be the id attribute
                * 2nd argument should be the size attribute
                * 3rd argument should be the x attribute
                * 4th argument should be the y attribute
              kwargs: must be skipped if *args exists and is not empty
        """
        for num in range(len(args)):
            setattr(self, 'id' if num == 0
                    else 'size' if num == 1
                    else 'x' if num == 2
                    else 'y', args[num])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Public method named to_dictionary
           Args:
               self: Variable referring to the same instance
           Returns:
               that returns the dictionary representation of a Square
        """
        dic = {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
        return dic
