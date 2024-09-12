#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add  # Importing the add function

    a = 1  # First variable
    b = 2  # Second variable

    # Print the result using formatted string
    print(f"{a} + {b} = {add(a, b)}")
