#!/usr/bin/python3
"""This module named 6-load_from_json_file.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


import json


def load_from_json_file(filename):
    """function named load_from_json_file
           Args:
               filename: The name of the input file
           Returns:
               An Object from a “JSON file”:
    """
    with open(filename, encoding='utf-8') as my_file:
        return json.loads(my_file.read())
