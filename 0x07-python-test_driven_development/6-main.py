#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))   # Expected output: 4
print(max_integer([1, 3, 4, 2]))   # Expected output: 4
print(max_integer([4, 3, 2, 1]))   # Expected output: 4
print(max_integer([4]))            # Expected output: 4
print(max_integer([]))             # Expected output: None
print(max_integer([-1, -2, -3, -4]))  # Expected output: -1
print(max_integer([1.5, 2.5, 3.5]))  # Expected output: 3.5
print(max_integer([1, 2, 2.5, 4]))   # Expected output: 4

try:
    print(max_integer())
except Exception as e:
    print(e)  # Expected to raise an exception if list is not provided
