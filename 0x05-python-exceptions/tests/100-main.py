#!/usr/bin/python3
safe_print_integer_err = __import__('100-safe_print_integer_err').safe_print_integer_err

# Test with an integer
value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

# Test with a negative integer
value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

# Test with a string (should fail)
value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
