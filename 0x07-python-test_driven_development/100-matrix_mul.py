#!/usr/bin/python3
"""
This module provides a function `matrix_mul` that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices (m_a and m_b).

    Args:
        m_a: The first matrix, must be a list of lists of integers or floats.
        m_b: The second matrix, must be a list of lists of integers or floats.

    Returns:
        A new matrix which is the result of multiplying m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers or floats.
        ValueError: If m_a or m_b is empty or if they can't be multiplied.
        TypeError: If the rows of m_a or m_b are not of the same size.
    """
    # Validate m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(item, (int, float)) for row in m_a for item in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(item, (int, float)) for row in m_b for item in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Matrix multiplication conditions
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform the multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            sum_result = 0
            for k in range(len(m_b)):
                sum_result += m_a[i][k] * m_b[k][j]
            row_result.append(sum_result)
        result.append(row_result)

    return result
