#!/usr/bin/python3
"""Task 6 : Create object from a JSON file """


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
