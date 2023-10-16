#!/usr/bin/python3
"""unittests for square.py"""
import unittest
from models.base import Base
from models.square import Square


class TestSquareInsta(unittest.TestCase):
    """unit test for the square class instantation"""
    def test_base(self):
        self.assertIsInstance(Square(8), Base)

    def test_rec(self):
        self.assertIsInstance(Square(8), Base)

    def test_unique_args(self):
        s1 = Square(8)
        s2 = Square(12)
        self.assertEqual(s1.id + 1, s2.id)

    def test_two_args(self):
        s1 = Square(8, 4)
        s2 = Square(4, 12)
        self.assertEqual(s1.id + 1, s2.id)
