#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

try:
    print(matrix_divided(matrix, 0))
except Exception as e:
    print(e)

try:
    print(matrix_divided([[1, 2], [4, 5, 6]], 2))
except Exception as e:
    print(e)

try:
    print(matrix_divided([[1, 2], ["a", 5]], 2))
except Exception as e:
    print(e)
