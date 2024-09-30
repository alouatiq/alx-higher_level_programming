#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        # Try to execute the function with the given arguments
        return fct(*args)
    except Exception as e:
        # If any exception occurs, print it to stderr with prefix 'Exception:'
        print("Exception: {}".format(e), file=sys.stderr)
        return None
