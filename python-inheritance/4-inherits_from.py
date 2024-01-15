#!/usr/bin/python3
"""Task 4 : Only sub class of """


def inherits_from(obj, a_class):
    """function that returns True if the object
       is an instance of a class that inherited """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
