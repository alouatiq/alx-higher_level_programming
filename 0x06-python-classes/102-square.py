#!/usr/bin/python3
"""
This module defines a class Square with comparison operations based on area.
"""


class Square:
    """A class that defines a square with size and can compare areas."""

    def __init__(self, size=0):
        """Initializes the square with size validation."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compares equality of two squares based on their area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Compares inequality of two squares based on their area."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Compares if the square is smaller than another based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Compares if the square is smaller or
        equal to another based on area.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """Compares if the square is greater than another based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Compares if the square is greater or
        equal to another based on area.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
