#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add  # Importing add function once

    a = 1  # Assign 1 to a
    b = 2  # Assign 2 to b

    # Print the result of add(a, b) using formatted string
    print("{} + {} = {}".format(a, b, add(a, b)))
