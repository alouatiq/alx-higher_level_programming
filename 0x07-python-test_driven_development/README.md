# 0x07. Python - Test-Driven Development
## Description
This project is part of the ALX Higher-Level Programming curriculum and focuses on Test-Driven Development (TDD) in Python. The primary goal of this project is to learn how to write tests before implementing code, ensuring that all edge cases and possible input scenarios are covered through automated testing.

Each task will follow TDD principles, including writing the tests first, then implementing the functions, and finally ensuring that the code passes all the tests.

## Learning Objectives
By the end of this project, you should be able to:

- Understand why Python programming is awesome.
- Explain the importance of tests in software development.
- Write Docstrings that generate tests.
- Write proper documentation for modules and functions.
- Create unit tests using Python’s ```unittest``` module.
- Identify and cover edge cases in test cases.

## Project Structure
The project directory is structured as follows:

```bash
/0x07-python-test_driven_development
│
├── README.md                # Project description
├── 0-add_integer.py         # Task 0: Integers addition function
├── 2-matrix_divided.py      # Task 1: Divide a matrix function
├── 3-say_my_name.py         # Task 2: Say my name function
├── 4-print_square.py        # Task 3: Print a square function
├── 5-text_indentation.py    # Task 4: Text indentation function
├── 6-max_integer.py         # Task 5: Max integer function
├── 100-matrix_mul.py        # Task 6: Matrix multiplication function (advanced)
├── 101-lazy_matrix_mul.py   # Task 7: Lazy matrix multiplication using NumPy (advanced)
├── 102-python.c             # Task 8: CPython #3: Python Strings (advanced)
│
├── tests                        # Directory for test cases
│   ├── 0-add_integer.txt        # Doctest for Task 0
│   ├── 2-matrix_divided.txt     # Doctest for Task 1
│   ├── 3-say_my_name.txt        # Doctest for Task 2
│   ├── 4-print_square.txt       # Doctest for Task 3
│   ├── 5-text_indentation.txt   # Doctest for Task 4
│   ├── 6-max_integer_test.py     # Unittest for Task 5
│   ├── 100-matrix_mul.txt        # Doctest for Task 6
│   ├── 101-lazy_matrix_mul.txt   # Doctest for Task 7
│   └── 102-tests.py              # Test script for Task 8 (C function for strings)
│
├── 0-main.py                # Main test file for Task 0 (Integers addition)
├── 2-main.py                # Main test file for Task 1 (Matrix division)
├── 3-main.py                # Main test file for Task 2 (Say my name)
├── 4-main.py                # Main test file for Task 3 (Print square)
├── 5-main.py                # Main test file for Task 4 (Text indentation)
├── 6-main.py                # Unittest for Task 5
├── 100-main.py              # Main test file for Task 6 (Matrix multiplication)
├── 101-main.py              # Main test file for Task 7 (Lazy matrix multiplication)
└── 102-tests.py             # Main test file for Task 8 (CPython strings)
```

