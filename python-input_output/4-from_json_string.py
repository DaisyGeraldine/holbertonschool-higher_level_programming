#!/usr/bin/python3
"""This module named 4-from_json_string.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


import json


def from_json_string(my_str):
    """function named write_file
           Args:
               my_str: a string
           Returns:
               an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
