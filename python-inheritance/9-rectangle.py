#!/usr/bin/python3
"""Task 9 : Full rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """Instantiation with width and height """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """Method calculate area"""
        return self.__width * self.__height

    def __str__(self):
        """return description: [Rectangle] <width>/<height> """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
