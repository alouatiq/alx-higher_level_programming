#!/usr/bin/python3
"""T10"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that
    inherits from Rectangle."""

    def __init__(self, size):
        """Initializes a square with the given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
