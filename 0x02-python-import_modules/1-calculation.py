#!/usr/bin/python3
if __name__ == "__main__":
    # Importing functions from calculator_1.py
    from calculator_1 import add, sub, mul, div

    # Assign values to a and b on separate lines
    a = 10
    b = 5

    # Use exactly 4 print statements to display the results
    print("{} + {} = {}".format(a, b, add(a, b)))  # Addition
    print("{} - {} = {}".format(a, b, sub(a, b)))  # Subtraction
    print("{} * {} = {}".format(a, b, mul(a, b)))  # Multiplication
    print("{} / {} = {}".format(a, b, div(a, b)))  # Division
