#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function

def my_div(a, b):
    return a / b

# Test: Division (valid)
result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

# Test: Division by zero (should raise an exception)
result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))

def print_list(my_list, length):
    i = 0
    while i < length:
        print(my_list[i])
        i += 1
    return len(my_list)

# Test: List printing (valid)
result = safe_function(print_list, [1, 2, 3, 4], 4)
print("result of print_list: {}".format(result))

# Test: List printing with out of range access (should raise an exception)
result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))
