#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div  # Import all functions from calculator_1.py

    a = 10  # Assign 10 to a
    b = 5   # Assign 5 to b

    # Perform calculations and print results using 4 print statements
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
