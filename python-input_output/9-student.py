#!/usr/bin/python3
"""This module named 9-student.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


class Student:
    """
    class Student that defines a student by
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys())}
