#!/usr/bin/python3
"""
This module defines a class called Square with a private attribute.
"""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """
        Initializes the square with a private size attribute.
        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private attribute
