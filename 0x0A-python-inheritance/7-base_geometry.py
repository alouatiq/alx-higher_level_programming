#!/usr/bin/python3
"""T7"""


class BaseGeometry:
    """BaseGeometry class with area and
    integer validation methods."""

    def area(self):
        """Raises an exception because
        it is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an
        integer and greater than 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
