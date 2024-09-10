#!/usr/bin/python3
print("{}".format("".join([chr(char) for char in range(97, 123) if chr(char) not in 'qe'])), end="")
