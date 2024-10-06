#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

# Expected output: [[ 7, 10], [15, 22]]
print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
# Expected output: [[13, 16]]
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

try:
    # Expected error: shape mismatch
    print(lazy_matrix_mul([[1, 2]], [[1, 2, 3]]))
except Exception as e:
    print(e)

try:
    print(lazy_matrix_mul(1, [[1, 2]]))  # Expected error: input is not a list
except Exception as e:
    print(e)
