#!/usr/bin/python3
import sys
import importlib

# Add the current directory to sys.path to allow importing files with numeric names
sys.path.append('.')

# Dynamically import the module
safe_print_integer_err = importlib.import_module('100-safe_print_integer_err').safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
