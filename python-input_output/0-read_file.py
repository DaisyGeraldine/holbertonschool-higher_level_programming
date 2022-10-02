#!/usr/bin/python3
"""This module named 0-read_file.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


def read_file(filename=""):
    """function named read_file
           Args:
               filename: file to read
           Returns:
               Nothing, also print file
    """
    with open(filename) as _file:
        print(_file.read())
