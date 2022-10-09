#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module named 1-Square.py
   Created on Saturday, October 08, 2022
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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method named save_to_file
           Args:
               cls: Is a instancie of class
               list_objs: is a list of instances who inherits of Base
           Returns:
               Nothing
        """
        filename = "{}.json".format(cls.__name__)
        list_dictionary = []

        if list_objs:
            for list_dict in list_objs:
                list_dictionary.append(list_dict.to_dictionary())
                format_json = cls.to_json_string(list_dictionary)
        else:
            format_json = cls.to_json_string(list_dictionary)

        with open(filename, 'w', encoding='utf-8') as my_file1:
            my_file1.write(format_json)

    @staticmethod
    def from_json_string(json_string):
        """ Static method named from_json_string
           Args:
               json_string: is a string representing a list of dictionaries
           Returns:
               The list of the JSON string representation json_string
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method named create
           Args:
               cls: Is a instancie of class
               dictionary: must be used as **kwargs of the method update
           Returns:
               An instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
