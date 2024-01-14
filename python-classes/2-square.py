#!/usr/bin/python3
""" Task 2 : Size validation
"""


class Square:
    """ class Square that defines a square """

    __size = 0

    def __init__(self, size=0):
        """Initializes the data.
            Arg:
                size must be an integer
                size must be less than or equal to zero
                otherwise: TypeError exception with the message
            return:
                __size
            """
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
