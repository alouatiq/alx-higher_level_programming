#!/usr/bin/python3
# Task 7: Manipulate a string by slicing and printing different parts
word = "Holberton"
word_first_3 = word[:3]  # First 3 letters of the string
word_last_2 = word[-2:]  # Last 2 letters of the string
middle_word = word[1:-1]  # Middle part of the string without the first and last letters
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")