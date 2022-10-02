#!/usr/bin/python3
"""This module named 2-append_write.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


def append_write(filename="", text=""):
    """function named write_file
           Args:
               filename: file to write
               text: text to write
           Returns:
               the number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as my_file:
        number_char = my_file.write(text)
        return number_char
