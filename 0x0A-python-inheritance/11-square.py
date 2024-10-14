#!/usr/bin/python3
"""T11"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from
    Rectangle with a custom str method."""

    def __init__(self, size):
        """Initializes a square with the given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns a formatted string description of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
