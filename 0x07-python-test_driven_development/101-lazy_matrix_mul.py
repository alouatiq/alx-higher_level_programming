#!/usr/bin/python3
"""
This module provides a function `lazy_matrix_mul` that multiplies two matrices using NumPy.
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
    return np.matmul(m_a, m_b)
