import importlib
#!/usr/bin/python3
safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers

# List of integers
my_list = [1, 2, 3, 4, 5]

# Test with the first 2 integers
nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

# Mixed list of integers and non-integers
my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

# Test with more elements than available
nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
