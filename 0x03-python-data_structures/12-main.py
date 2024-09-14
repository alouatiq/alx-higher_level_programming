# This script just executes the switch operation and prints the result.
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
