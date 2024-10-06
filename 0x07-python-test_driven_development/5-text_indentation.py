#!/usr/bin/python3
"""
This module provides a function `text_indentation`
that adds two new lines after `.`, `?`, and `:`.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of
    these characters: `.`, `?`, and `:`.

    Args:
        text: A string to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Handle empty string case by printing a blank line
    if text == "":
        print()
        return

    # Remove leading/trailing spaces and format text
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            i += 1
            # Skip any following space characters
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
