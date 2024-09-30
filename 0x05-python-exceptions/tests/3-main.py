import importlib
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

# Test with valid division
a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

# Test division by zero
a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
