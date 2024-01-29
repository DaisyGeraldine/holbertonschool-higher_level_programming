#!/usr/bin/python3
"""Task 3 : To JSON string """


import json


def to_json_string(my_obj):
    """function named write_file
           Args:
               my_obj: an object data structure
           Returns:
               the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
