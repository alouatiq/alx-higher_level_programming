#!/usr/bin/python3
"""
This module defines a class Square with size validation and an area method.
"""


class Square:
    """A class that defines a square by its size and can calculate its area."""

    def __init__(self, size=0):
        """Initializes the square, with validation for size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
