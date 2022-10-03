#!/usr/bin/python3
"""This module named 4-from_json_string.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


import json


def save_to_json_file(my_obj, filename):
    """function named write_file
           Args:
               my_obj: The inputed object to convert in json format
               filename: The name of the output file
           Returns:
               write a file JSON representation
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(json.dumps(my_obj))
