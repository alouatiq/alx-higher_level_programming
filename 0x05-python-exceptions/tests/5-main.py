import importlib
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

# Test to check if TypeError is raised
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
