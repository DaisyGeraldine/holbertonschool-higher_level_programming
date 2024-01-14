#!/usr/bin/python3
""" Task 1 : Square with size
"""


class Square:
    """ class Square that defines a square
        Private instance attribute: size """
    __size = 0

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
