#!/usr/bin/python3
""" Task 4 : Access and update private attribute
"""


class Square:
    """ class Square that defines a square by: (based on 3-square.py) """

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
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter method to set the size."""
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method that returns the current square area """
        return self.__size * self.__size
