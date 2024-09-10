#!/usr/bin/python3
print("".join(["%c" % (i - 32 if i % 2 else i) for i in range(122, 96, -1)]), end="")
