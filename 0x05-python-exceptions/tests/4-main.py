import importlib
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

# Test with valid lists
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, 3)
print(result)

print("--")

# Test with various issues (zero division, wrong type, out of range)
my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, 5)
print(result)
