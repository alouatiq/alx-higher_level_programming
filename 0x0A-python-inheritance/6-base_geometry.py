#!/usr/bin/python3
"""T6"""


class BaseGeometry:
    """BaseGeometry class with an
    unimplemented area method."""

    def area(self):
        """Raises an exception because it
        is not implemented."""
        raise Exception("area() is not implemented")
