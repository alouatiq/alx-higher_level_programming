#!/usr/bin/python3
for i in range(122, 96, -1):  # ASCII values from 'z' (122) to 'a' (97)
    if i % 2 == 0:  # Even ASCII values should be lowercase
        print("{}".format(chr(i)), end="")
    else:  # Odd ASCII values should be uppercase
        print("{}".format(chr(i - 32)), end="")
