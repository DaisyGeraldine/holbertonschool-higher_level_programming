#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module 0-add_integer.py

   Created on Saturday, September 24, 2022

   @author: Daisy Chipana Lapa
"""


def add_integer(a, b=98):
    """function add two numbers
        Args:
             a: is first parameter
             b: is second parameter
        Returns:
             Sum two numbers cast as integers
        """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    suma = a + b
    return int(a + b)
