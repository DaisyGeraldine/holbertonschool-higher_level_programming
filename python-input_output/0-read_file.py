#!/usr/bin/python3
"""This module named 0-read_file.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


def read_file(filename=""):
    with open('my_file_0.txt') as _file:
        print(_file.read())
