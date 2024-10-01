#!/usr/bin/python3
"""
This module defines a class Square with size validation, getters, and setters.
"""


class Square:
    """
    A class that defines a square with
    private size and a public area method.
    """

    def __init__(self, size=0):
        """Initializes the square, with size validation."""
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square, with validation.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
