import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]

s = "The spoon does not exist"
lib.print_python_string(s)  # Expected output: string info

s = "ложка не существует"
lib.print_python_string(s)  # Expected output: string info

s = "La cuillère n'existe pas"
lib.print_python_string(s)  # Expected output: string info

s = "勺子不存在"
lib.print_python_string(s)  # Expected output: string info

s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)  # Expected output: string info

s = "スプーンは存在しない"
lib.print_python_string(s)  # Expected output: string info

s = b"The spoon does not exist"  # Expected error: invalid string
lib.print_python_string(s)


