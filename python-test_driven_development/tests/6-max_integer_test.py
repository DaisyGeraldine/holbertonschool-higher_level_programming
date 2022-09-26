#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list_positive(self):
        """Thid methods find the max list positive"""
        lista = max_integer([4, 5, 8, 2])
        self.assertEqual(lista, 8)

    def test_list_negative(self):
        """Thid methods find the max list negative"""
        lista = max_integer([-4, 5, -8, 2])
        self.assertEqual(lista, 5)

    def test_list_empty(self):
        """Thid methods find the max list empty"""
        lista = max_integer([])
        self.assertEqual(lista, None)

    def test_list_float(self):
        """Thid methods find the max list empty"""
        lista = max_integer([5.2, 4.8, 1.3, 5])
        self.assertEqual(lista, 5.2)
