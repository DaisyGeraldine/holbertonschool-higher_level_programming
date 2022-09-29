#!/usr/bin/python3
"""This module named 2-is_same_class
   Created on Thursday, September 29, 2022
   @author: Daisy Chipana Lapa
"""


def is_kind_of_class(obj, a_class):
    """Function named is_same_class
          Args:
             obj: objeto to validate
             a_class: class
          Returns:
             True if is instance of the specified class or if the object
             is an instance of a class that inherited from, otherwise False
    """
    return isinstance(obj, a_class)
