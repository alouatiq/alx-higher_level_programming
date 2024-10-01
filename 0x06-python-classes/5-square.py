#!/usr/bin/python3
"""
This module defines a class Square with size
validation, getters, setters, and printing.
"""


class Square:
    """
    A class that defines a square with private
    size, an area method, and printing.
    """

    def __init__(self, size=0):
        """Initializes the square, with size validation."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #
        or an empty line if size is 0.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
