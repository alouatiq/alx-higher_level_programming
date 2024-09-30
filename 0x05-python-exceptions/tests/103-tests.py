import importlib
#!/usr/bin/python3 -u

import ctypes

lib = ctypes.CDLL('./libPython.so')

# Set function signatures
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]

# Test bytes
s = b"Hello"
lib.print_python_bytes(s)

b = b'\xff\xf8\x00\x00\x00\x00\x00\x00'
lib.print_python_bytes(b)

b = b"What does the 'b' character do in front of a string literal?"
lib.print_python_bytes(b)

# Test list
l = [b'Hello', b'World']
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)

# Test float
f = 3.14
lib.print_python_float(f)

# Test list with mixed elements
l = [-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159]
lib.print_python_list(l)
