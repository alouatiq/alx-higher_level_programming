import importlib
#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function

# Test with a valid function
def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

# Test with division by zero
result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))

# Test with another function that raises an index error
def print_list(my_list, length):
    for i in range(length):
        print(my_list[i])
    return len(my_list)

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))
