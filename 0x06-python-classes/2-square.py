#!/usr/bin/python3
"""
This module defines a class Square with size validation.
"""


class Square:
    """A class that defines a square by its size and validates it."""

    def __init__(self, size=0):
        """
        Initializes the square with a size attribute,
        ensuring it's an integer and >= 0.
        Args:
            size (int): The size of the square (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
