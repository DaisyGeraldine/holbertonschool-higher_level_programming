#!/usr/bin/python3
"""This module named 8-class_to_json.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


def class_to_json(obj):
    """function named load_from_json_file
           Args:
               obj: Is an instance of a Class
           Returns:
               The dictionary description with simple data structure
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
