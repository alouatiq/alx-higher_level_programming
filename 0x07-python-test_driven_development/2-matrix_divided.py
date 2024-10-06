#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    
    Args:
        matrix: A list of lists of integers or floats (must be rectangular).
        div: The divisor, must be an integer or float, and cannot be 0.
    
    Returns:
        A new matrix with each element of the original matrix divided by div,
        rounded to 2 decimal places.
    
    Raises:
        TypeError: If matrix elements are not integers/floats
        or if rows are of unequal length.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise ValueError("matrix can't be empty")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(item / div, 2) for item in row] for row in matrix]
