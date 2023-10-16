#!/usr/bin/python3
"""unittests for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_Insta(unittest.TestCase):
    """unit test for the base class instantation"""
    def test_unique_id(self):
        """test method to check if id are unique"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_none_arg(self):
        """test method to check if id is None"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id + 1, b2.id)

    def test_id_12(self):
        """test method to check if the id attribute of an instance of
        the Base class, created with the argument 12, is equal to 12"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)


class TestBase_to_json(unittest.TestCase):
    """unit test for testing to_json_string"""
    def test_to_jsoon_string_rectangle(self):
        rec = Rectangle(10, 7, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))


class TestBase_from_json(unittest.TestCase):
    """unit test for testing from_json_string"""
    def test_from_json_rectangle(self):
        list_in = [{"width": 10, "height": 5, "id": 16}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)


if __name__ == "__main__":
    unittest.main()
