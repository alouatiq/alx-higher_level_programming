#!/usr/bin/python3
"""Unittest for Square class"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_square_init(self):
        """Test initialization of the Square class"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_area(self):
        """Test area calculation"""
        s = Square(6)
        self.assertEqual(s.area(), 36)

    def test_invalid_size(self):
        """Test invalid size raises TypeError"""
        with self.assertRaises(TypeError):
            s = Square("5")

    def test_update(self):
        """Test update with *args"""
        s = Square(5)
        s.update(10, 7)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)


if __name__ == "__main__":
    unittest.main()
