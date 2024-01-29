#!/usr/bin/python3
"""Task 4 : From JSON string to Object """


import json


def from_json_string(my_str):
    """function named write_file
           Args:
               my_str: a string
           Returns:
               an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
