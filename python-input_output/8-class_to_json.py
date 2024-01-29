#!/usr/bin/python3
"""Task 8 : Class to JSON """


def class_to_json(obj):
    """function named load_from_json_file
           Args:
               obj: Is an instance of a Class
           Returns:
               The dictionary description with simple data structure
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
