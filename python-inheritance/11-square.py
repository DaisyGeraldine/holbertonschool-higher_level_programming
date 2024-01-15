#!/usr/bin/python3
"""Task 11 : Square #2 """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle """
    def __init__(self, size):
        """Instantiation with size """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method calculate area"""
        return super().area()

    def __str__(self):
        """return description: [Square] <width>/<height> """
        return '[Square] {}/{}'.format(self.__size, self.__size)
