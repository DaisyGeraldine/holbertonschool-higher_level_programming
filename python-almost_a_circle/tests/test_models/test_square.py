#!/usr/bin/python3
"""Unittest for class Square()
"""
import unittest
import io
import sys
import json
from models.square import Square


class Test_Rectangle(unittest.TestCase):
    def test_Square_one_argument(self):
        """This methods will be tested one one_arguments"""
        s1 = Square(13)
        s2 = Square(4)
        self.assertEqual(s1.size, 13)
        self.assertEqual(s2.size, 4)

    def test_Square_arguments(self):
        """This methods will be tested one two_arguments"""
        s1 = Square(10, 2)
        s2 = Square(4, 1)
        s3 = Square(8, 1, 2)
        s4 = Square(8, 1, 2, 4)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s2.size, 4)
        self.assertEqual(s3.size, 8)
        self.assertEqual(s4.id, 4)


class Test_Square_validate_atributes(unittest.TestCase):
    def test_Square_str(self):
        """This methods will be tested with str value"""
        with self.assertRaises(TypeError):
            s1 = Square("1")

    def test_Square_negative(self):
        """This methods will be tested with a negative number"""
        with self.assertRaises(ValueError):
            s1 = Square(-12)
        with self.assertRaises(ValueError):
            s2 = Square(10, -2)
        with self.assertRaises(ValueError):
            s3 = Square(1, 2, -3)

    def test_Square_zero(self):
        """This methods will be tested with a zero"""
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_Square_if_x_str(self):
        """This methods will be tested with the atribute x as str"""
        with self.assertRaises(TypeError):
            s1 = Square(10, 5, "2")
        with self.assertRaises(TypeError):
            s2 = Square(5, 10, "3")


class Test_Square__str__exist(unittest.TestCase):
    def test_Square_str__exist(self):
        """This methods will be tested in case of function __str__"""
        s1 = Square(4, 6, 2, 1)
        self.assertEquals(str(s1), '[Square] (1) 6/2 - 4')


class Test_Square_display(unittest.TestCase):
    def test_Square_display_exist(self):
        """This methods will be tested in case if display exist"""
        output = io.StringIO()
        sys.stdout = output
        s1 = Square(4, 2, 2)
        s1.display()
        prints = "\n\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEquals(output.getvalue(), prints)


class Test_Square_to_dictionary(unittest.TestCase):
    def test_Square_to_dictionary(self):
        """This methods will be tested if Square exist"""
        s10 = Square(10, 2, 1, 9)
        s1_dictionary = s10.to_dictionary()
        self.assertEqual(s1_dictionary['size'], 10)
        self.assertEqual(s1_dictionary['x'], 2)
        self.assertEqual(s1_dictionary['y'], 1)
        self.assertEqual(s1_dictionary['id'], 9)


class Test_Square_update(unittest.TestCase):
    def test_Square_update_args(self):
        """This methods will be tested with Update args"""
        s1 = Square(10, 10, 10)
        s1.id = 1
        self.assertEqual(str(s1), '[Square] (1) 10/10 - 10')
        s1.update(89)
        self.assertEqual(str(s1), '[Square] (89) 10/10 - 10')
        s1.update(89, 2)
        self.assertEqual(str(s1), '[Square] (89) 10/10 - 2')
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), '[Square] (89) 3/10 - 2')
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (89) 3/4 - 2')

    def test_Square_update_kwargs(self):
        """This methods will be tested with Update kwargs"""
        s1 = Square(10, 10, 10, 10)
        s1.id = 1
        s1.update(size=1)
        self.assertEqual(str(s1), '[Square] (1) 10/10 - 1')
        s1.update(size=1, x=2)
        self.assertEqual(str(s1), '[Square] (1) 2/10 - 1')
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(s1), '[Square] (89) 3/1 - 2')
        s1.update(x=1, size=2, y=3, width=4)
        self.assertEqual(str(s1), '[Square] (89) 1/3 - 2')
