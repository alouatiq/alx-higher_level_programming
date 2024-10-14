#!/usr/bin/python3
"""T8"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that
    inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes width and height
        validating them as positive integers."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
