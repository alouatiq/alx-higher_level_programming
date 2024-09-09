#!/usr/bin/python3
# Task 8: Concatenate specific parts of a long string to form a new sentence
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
# Print the new sentence by slicing and concatenating parts of the original string
print(str[39:67] + str[107:112] + str[:6])
