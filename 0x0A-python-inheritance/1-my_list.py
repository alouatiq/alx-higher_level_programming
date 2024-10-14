#!/usr/bin/python3
"""Module for task 1"""


class MyList(list):
    """
    Inherits from list with additional
    print_sorted method
    """

    def print_sorted(self):
        """
        Prints the list in ascending
        sorted order
        """
        print(sorted(self))
