#!/usr/bin/python3
"""Task 10 : Square #1 """
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
