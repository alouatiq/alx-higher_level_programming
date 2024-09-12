#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Ensure the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Retrieve arguments from the command line
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Define the supported operations
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    # Check if the operator is valid
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform the calculation
    result = operations[operator](a, b)

    # Print the result in the specified format
    print(f"{a} {operator} {b} = {result}")
