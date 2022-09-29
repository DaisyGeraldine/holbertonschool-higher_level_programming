#!/usr/bin/python3
"""This module named 4-inherits_from
   Created on Thursday, September 29, 2022
   @author: Daisy Chipana Lapa
"""


def inherits_from(obj, a_class):
    """Function named inherits_from
          Args:
             obj: objeto to validate
             a_class: class
          Returns:
             True if if the object is an instance of, or if the object
             is an instance of a class that inherited from, the specified
             class ;otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
