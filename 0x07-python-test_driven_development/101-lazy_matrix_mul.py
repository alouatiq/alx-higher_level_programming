#!/usr/bin/python3
"""
This module provides a function `lazy_matrix_mul`
that multiplies two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: The first matrix, must be a list of lists of integers or floats.
        m_b: The second matrix, must be a list of lists of integers or floats.

    Returns:
        A new matrix which is the result of multiplying m_a by m_b using NumPy.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers or floats.
        ValueError: If m_a or m_b can't be multiplied.
    """
    # Check if m_a and m_b are lists of lists
    if not isinstance(
        m_a,
        list) or not all(
        isinstance(
            row,
            list) for row in m_a):
        raise TypeError("m_a must be a list of lists of integers or floats")
    if not isinstance(
        m_b,
        list) or not all(
        isinstance(
            row,
            list) for row in m_b):
        raise TypeError("m_b must be a list of lists of integers or floats")

    # Use NumPy to perform matrix multiplication
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        if "scalar operands" in str(e):
            raise TypeError(
                "matmul: Input must be a list of lists of integers or floats")
        raise
