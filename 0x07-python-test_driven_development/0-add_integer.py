#!/usr/bin/python3
"""
This module provides a function `add_integer` that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if necessary.

    Args:
        a: The first number, must be an integer or a float.
        b: The second number, must be an integer or a float (defaults to 98).

    Returns:
        The sum of a and b, casted to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
