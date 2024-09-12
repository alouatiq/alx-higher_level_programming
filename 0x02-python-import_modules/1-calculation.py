#!/usr/bin/python3
if __name__ == "__main__":
    # Import the required functions from calculator_1 (word calculator_1 used only once)
    from calculator_1 import add, sub, mul, div

    # Define a and b on two different lines
    a = 10
    b = 5

    # Perform calculations and print results, ensuring only 4 print statements
    print("{} + {} = {}".format(a, b, add(a, b)))  # Addition
    print("{} - {} = {}".format(a, b, sub(a, b)))  # Subtraction
    print("{} * {} = {}".format(a, b, mul(a, b)))  # Multiplication
    print("{} / {} = {}".format(a, b, div(a, b)))  # Division
