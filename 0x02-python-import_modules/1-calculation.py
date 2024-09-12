#!/usr/bin/python3
if __name__ == "__main__":
    # Import only once from calculator_1
    from calculator_1 import add, sub, mul, div

    # Assign values to a and b on two separate lines
    a = 10
    b = 5

    # Perform calculations and print results (only 4 print statements)
    print("{} + {} = {}".format(a, b, add(a, b)))  # Addition
    print("{} - {} = {}".format(a, b, sub(a, b)))  # Subtraction
    print("{} * {} = {}".format(a, b, mul(a, b)))  # Multiplication
    print("{} / {} = {}".format(a, b, div(a, b)))  # Division
