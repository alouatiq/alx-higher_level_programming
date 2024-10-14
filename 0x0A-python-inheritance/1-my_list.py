#!/usr/bin/python3
class MyList(list):
    """A class that inherits from list with a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending)."""
        print(sorted(self))
