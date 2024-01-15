#!/usr/bin/python3
"""Task 7 : Integer validator """


class BaseGeometry:
    """BaseGeometry class """
    def area(self):
        """that raises an Exception with the message """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Method that validates value"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
