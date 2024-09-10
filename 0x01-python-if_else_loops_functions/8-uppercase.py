#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # If the character is lowercase (between 'a' and 'z')
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert to uppercase by subtracting 32 from its ASCII value
            char = chr(ord(char) - 32)
        # Print the character without a newline
        print("{}".format(char), end="")
    # Print a newline after the loop
    print()
