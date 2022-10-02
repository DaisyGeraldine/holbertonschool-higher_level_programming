#!/usr/bin/python3
"""This module named 1-write_file.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


def write_file(filename="", text=""):
    """function named write_file
           Args:
               filename: file to write
               text: text to write
           Returns:
               the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as my_file:
        number_char = my_file.write(text)
        return number_char
