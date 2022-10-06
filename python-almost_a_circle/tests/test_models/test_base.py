#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    def test_Base_Id(self):
        """This methods create a id secuential"""
        b1 = Base(5)
        b2 = Base(12)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 12)

    def test_Base_Empty(self):
        """This methods create a id Empty"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_Base_Negative(self):
        """This methods create a id Negative"""
        b1 = Base(-5)
        b2 = Base(-13)
        self.assertEqual(b1.id, -5)
        self.assertEqual(b2.id, -13)
