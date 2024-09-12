#!/usr/bin/python3
if __name__ == "__main__":
    # Importing functions from calculator_1.py
    from calculator_1 import add, sub, mul, div

    # Assigning values to a and b on two different lines
    a = 10
    b = 5

    # Perform calculations and print results
    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = int(div(a, b))  # Ensure result is an integer

    # Printing results (with exactly 4 print statements)
    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_sub))
    print("{} * {} = {}".format(a, b, result_mul))
    print("{} / {} = {}".format(a, b, result_div))  # Ensure division result is an integer
