#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    def test_Rectangle_arguments_exist(self):
        """This methods will be tested with all_arguments"""
        r1 = Rectangle(10, 2, 1, 1, 12)
        #self.assertEqual(r1, (10, 2, 0, 0, 12))

    def test_Rectangle_all_arguments(self):
        """This methods will be tested with all_arguments"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(2, 10, 0, 0, 5)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r2.id, 5)

    def test_Rectangle_two_arguments(self):
        """This methods will be tested with two_arguments"""
        r1 = Rectangle(13, 2)
        r2 = Rectangle(5, 4)
        r1.id = 1
        self.assertEqual(r1.id, 1)
        r2.id = 2
        self.assertEqual(r2.id, 2)

class Test_Rectangle_validate_atributes(unittest.TestCase):
    def test_Rectangle_str(self):
        """This methods will be tested with str value"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")

    def test_Rectangle_negative_or_zero(self):
        """This methods will be tested with a negative number"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.width = -10
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.width = 0

class Test_Rectangle_Area_first(unittest.TestCase):
    def test_Rectangle_area_number_positive(self):
        """This methods will be tested with numbers positive"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)
