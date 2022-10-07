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
