#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
op = sys.argv[2]
b = int(sys.argv[3])

ops = {"+": add, "-": sub, "*": mul, "/": div}

if op not in ops:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

result = ops[op](a, b)
print("{} {} {} = {}".format(a, op, b, result))
