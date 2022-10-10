#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    def test_Rectangle_arguments_exist(self):
        """This methods will be tested with all_arguments"""
        r1 = Rectangle(1, 2)
        self.assertEqual((r1.width, r1.height), (1, 2))

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

    def test_Rectangle_negative(self):
        """This methods will be tested with a negative number"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -12)
        with self.assertRaises(ValueError):
            r2 = Rectangle(-11, 2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)

    def test_Rectangle_zero(self):
        """This methods will be tested with a zero"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 2)

    def test_Rectangle_if_x_str(self):
        """This methods will be tested with the atribute x as str"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 5, "2")
        with self.assertRaises(TypeError):
            r2 = Rectangle(5, 10, "3")

    def test_Rectangle_if_y_str(self):
        """This methods will be tested with the atribute y as str"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 5, 2, "2")
        with self.assertRaises(TypeError):
            r2 = Rectangle(5, 10, 3, "3")

class Test_Rectangle_Area_first(unittest.TestCase):
    def test_Rectangle_area_number_positive(self):
        """This methods will be tested with numbers positive"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

class Test_Rectangle__str__exist(unittest.TestCase):
    def test_Rectangle_str__exist(self):
        """This methods will be tested in case of function __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEquals(str(r1), '[Rectangle] (12) 2/1 - 4/6')
