#!/usr/bin/python3
"""unittests for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInsta(unittest.TestCase):
    """unit test for the rectangle class instantaion"""
    def test_unique_args(self):
        """test in case if there's only one argument passed"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """test in case if there's two argument passed"""
        rec1 = Rectangle(3, 3, 6)
        rec2 = Rectangle(6, 6, 2)
        self.assertEqual(rec1.id + 1, rec2.id)
