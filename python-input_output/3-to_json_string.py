#!/usr/bin/python3
"""This module named 3-to_json_string.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


import json


def to_json_string(my_obj):
    """function named write_file
           Args:
               my_obj: an object data structure
           Returns:
               the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
