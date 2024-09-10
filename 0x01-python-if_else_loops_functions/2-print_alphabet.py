#!/usr/bin/python3
# Using a for loop with the range of ASCII values for lowercase letters
print("{}".format("".join(chr(i) for i in range(97, 123))), end="")
