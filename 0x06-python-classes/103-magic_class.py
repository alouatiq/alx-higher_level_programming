#!/usr/bin/python3
import math
"""
This module defines a class MagicClass based on the provided bytecode.
"""


class MagicClass:
    """
    A class that represents a circle with
    a radius and calculates area and circumference.
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass with a radius.
        Args:
            radius (float or int): The radius of the circle (default is 0).
        Raises:
            TypeError: If radius is not a number (float or int).
        """
        self.__radius = 0  # Set default radius to 0
        if type(radius) not in [int, float]:  # Check if radius is a number
            raise TypeError("radius must be a number")
        self.__radius = radius  # Set the radius if the type is valid

    def area(self):
        """
        Calculates the area of the circle.
        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2) * math.pi  # Return area: pi * r^2

    def circumference(self):
        """
        Calculates the circumference of the circle.
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius  # Return circumference: 2 * pi * r
