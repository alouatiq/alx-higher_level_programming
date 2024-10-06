#!/usr/bin/python3
"""
This module defines a function matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide the elements by.

    Returns:
        A new matrix where each element is divided
        by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   If each row of the matrix is not the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(
        matrix,
        list) or not all(
        isinstance(
            row,
            list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
