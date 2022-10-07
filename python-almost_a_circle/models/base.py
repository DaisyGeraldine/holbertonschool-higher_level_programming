#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module named 1-Square.py
   Created on Wednesday, October 05, 2022
   @author: Daisy Chipana Lapa
"""


import json


class Base:
    """This class is named Base
    Attributes:
       __nb_objects: private class attribute, increment.
       This class will be the “base” of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method named to_json_string
           Args:
               list_dictionaries: is a list of dictionaries
           Returns:
               the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
