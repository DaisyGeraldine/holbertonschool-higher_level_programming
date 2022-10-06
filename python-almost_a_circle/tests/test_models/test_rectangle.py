#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    def test_Rectangle_two_arguments(self):
        """This methods will be tested with two_arguments"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_Rectangle_all_arguments(self):
        """This methods will be tested with all_arguments"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(2, 10, 0, 0, 5)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r2.id, 5)
