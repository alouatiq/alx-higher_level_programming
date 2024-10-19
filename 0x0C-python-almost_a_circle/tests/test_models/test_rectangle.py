#!/usr/bin/python3
"""Unittest for Rectangle class"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_rectangle_init(self):
        """Test initialization of the Rectangle class"""
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

    def test_area(self):
        """Test area calculation"""
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

    def test_invalid_width(self):
        """Test invalid width raises TypeError"""
        with self.assertRaises(TypeError):
            r = Rectangle("10", 2)

    def test_invalid_height(self):
        """Test invalid height raises ValueError"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, -2)


if __name__ == "__main__":
    unittest.main()
