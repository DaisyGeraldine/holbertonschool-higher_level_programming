#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module 3-say_my_name.py
   Created on Sunday, September 25, 2022
   @author: Daisy Chipana Lapa
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>
        Args:
             first_name: String Characteres
             last_name: String Characteres
        Returns:
             Print first name and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print('My name is {} {}'.format(first_name, last_name))
