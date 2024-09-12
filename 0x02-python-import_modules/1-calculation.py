#!/usr/bin/python3
if __name__ == "__main__":
    # Import functions from calculator_1
    from calculator_1 import add, sub, mul, div

    a = 10  # Variable a is 10
    b = 5   # Variable b is 5

    # Print results for each mathematical operation
    print("{} + {} = {}".format(a, b, add(a, b)))  # Addition
    print("{} - {} = {}".format(a, b, sub(a, b)))  # Subtraction
    print("{} * {} = {}".format(a, b, mul(a, b)))  # Multiplication
    print("{} / {} = {}".format(a, b, div(a, b)))  # Division
