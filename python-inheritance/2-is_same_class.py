#!/usr/bin/python3
"""This module named 2-is_same_class
   Created on Thursday, September 29, 2022
   @author: Daisy Chipana Lapa
"""


def is_same_class(obj, a_class):
    """Function named is_same_class
          Args:
             obj: objeto to validate
             a_class: class
          Returns:
             True if is instance of the specified class, otherwise False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
