#!/usr/bin/python3
"""
Unittests for max_integer([..]).
"""
import unittest
import importlib.util
import os

# Dynamically load the '6-max_integer.py' file
spec = importlib.util.spec_from_file_location("max_integer", os.path.join(os.path.dirname(__file__), "../6-max_integer.py"))
max_integer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(max_integer)


class TestMaxInteger(unittest.TestCase):
    """Define test cases for the max_integer function"""

    def test_max_at_end(self):
        """Test when the max integer is at the end of the list"""
        self.assertEqual(max_integer.max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test when the max integer is at the beginning of the list"""
        self.assertEqual(max_integer.max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test when the max integer is in the middle of the list"""
        self.assertEqual(max_integer.max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        """Test a list with only one element"""
        self.assertEqual(max_integer.max_integer([5]), 5)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer.max_integer([]), None)

    def test_floats(self):
        """Test a list of floats"""
        self.assertEqual(max_integer.max_integer([1.2, 2.8, 3.5, 0.5]), 3.5)

    def test_mixed(self):
        """Test a list of mixed data types (integers and floats)"""
        self.assertEqual(max_integer.max_integer([1, 2.5, 3, 4.7]), 4.7)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer.max_integer([-1, -2, -3, -4]), -1)

    def test_all_same(self):
        """Test a list where all elements are the same"""
        self.assertEqual(max_integer.max_integer([3, 3, 3, 3]), 3)


if __name__ == "__main__":
    unittest.main()
