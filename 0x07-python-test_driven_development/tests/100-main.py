#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

try:
    print(matrix_mul([[1, 2]], [[1, 2, 3]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul(1, [[1, 2]]))
except Exception as e:
    print(e)
