#!/usr/bin/python3
"""Unittest for Base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_id_auto_increment(self):
        """Test auto-increment of id when id is not provided"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_custom_id(self):
        """Test custom id assignment"""
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_to_json_string(self):
        """Test JSON string conversion"""
        dictionary = {"id": 1, "width": 10, "height": 5}
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(type(json_string), str)
        self.assertIn('"width": 10', json_string)

    def test_from_json_string(self):
        """Test conversion from JSON string to list"""
        json_string = '[{"id": 1, "width": 10}]'
        dictionary_list = Base.from_json_string(json_string)
        self.assertEqual(dictionary_list[0]["width"], 10)


if __name__ == "__main__":
    unittest.main()
