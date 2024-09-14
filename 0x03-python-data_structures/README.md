# 0x03. Python - Data Structures: Lists, Tuples

This repository contains the solutions for the project **"0x03. Python - Data Structures: Lists, Tuples"** from the ALX Higher Level Programming curriculum.

The project focuses on various data structures in Python, such as lists and tuples, and implements basic operations and algorithms to manipulate them.

---

## Table of Contents

- [Files](#files)
- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Usage](#usage)

---

## Files

| Filename                  | Description                                             |
|---------------------------|---------------------------------------------------------|
| `0-print_list_integer.py`  | Prints all integers of a list                           |
| `1-element_at.py`          | Retrieves an element from a list like in C              |
| `2-replace_in_list.py`     | Replaces an element of a list at a specific position    |
| `3-print_reversed_list_integer.py` | Prints all integers of a list, in reverse order  |
| `4-new_in_list.py`         | Replaces an element in a copy of a list                 |
| `5-no_c.py`                | Removes all characters `c` and `C` from a string        |
| `6-print_matrix_integer.py`| Prints a matrix of integers                             |
| `7-add_tuple.py`           | Adds 2 tuples                                           |
| `8-multiple_returns.py`    | Returns the length of a string and its first character  |
| `9-max_integer.py`         | Finds the biggest integer of a list                     |
| `10-divisible_by_2.py`     | Finds all multiples of 2 in a list                      |
| `11-delete_at.py`          | Deletes the item at a specific position in a list       |
| `12-switch.py`             | Switches the values of two variables                    |
| `13-is_palindrome.c`       | Checks if a singly linked list is a palindrome (in C)   |
| `lists.h`                  | Header file for Task 13 (C code)                        |
| `linked_lists.c`           | Helper functions for Task 13 (C code)                   |
| `100-print_python_list_info.c` | Prints basic info about Python lists (in C)         |
| `main.py`                  | Main files to test each task                            |

---

## Description

This project covers the following topics:

- Python data structures, including lists and tuples
- Accessing and manipulating elements within lists
- Basic tuple operations
- Reversing lists, replacing elements, and more
- Working with C to manipulate linked lists
- Using C to explore how Python's internal list structures work

---

## Learning Objectives

By completing this project, you should be able to:

- Understand the concepts of lists and tuples in Python.
- Know how to access and modify elements in lists.
- Use slicing to extract sublists.
- Write functions to manipulate data structures.
- Understand basic memory management in Python when dealing with lists.
- Use basic algorithms to reverse lists, replace elements, and search for values.
- Write and manipulate linked lists in C.
- Work with Python lists using C through the Python/C API.

---

## Requirements

### Python
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Your code should use the PEP 8 style guide (version 1.7.x)
- You are not allowed to import any external libraries, unless explicitly stated in the task
- All your files should end with a new line

### C (for Task 13 & 14)
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using `gcc`, with the following options: `-Wall -Werror -Wextra -pedantic -std=gnu89`
- You are not allowed to use global variables
- You are allowed to use the standard library
- Your code should follow the Betty coding style

---

## Tasks

### Task 0: Print a list of integers
- Write a function `print_list_integer(my_list=[])` that prints all integers in a list.

### Task 1: Secure access to an element in a list
- Write a function `element_at(my_list, idx)` that retrieves an element from a list.

### Task 2: Replace element
- Write a function `replace_in_list(my_list, idx, element)` that replaces an element in a list.

### Task 3: Print a list of integers... in reverse!
- Write a function `print_reversed_list_integer(my_list=[])` that prints all integers in a list, in reverse order.

### Task 4: Replace in a copy
- Write a function `new_in_list(my_list, idx, element)` that replaces an element in a list without modifying the original list.

### Task 5: Remove `c` and `C` from a string
- Write a function `no_c(my_string)` that removes all characters `c` and `C` from a string.

### Task 6: Print a matrix of integers
- Write a function `print_matrix_integer(matrix=[[]])` that prints a matrix of integers.

### Task 7: Add two tuples
- Write a function `add_tuple(tuple_a=(), tuple_b=())` that adds two tuples.

### Task 8: More returns!
- Write a function `multiple_returns(sentence)` that returns a tuple with the length of a string and its first character.

### Task 9: Find the max
- Write a function `max_integer(my_list=[])` that finds the largest integer in a list.

### Task 10: Only by 2
- Write a function `divisible_by_2(my_list=[])` that finds all multiples of 2 in a list.

### Task 11: Delete at
- Write a function `delete_at(my_list=[], idx=0)` that deletes an item at a specific position in a list.

### Task 12: Switch values of `a` and `b`
- Write a script that switches the values of two variables.

### Task 13: Linked list palindrome (C)
- Write a function `is_palindrome(listint_t **head)` in C that checks if a singly linked list is a palindrome.

### Task 14: CPython #0: Python lists (C)
- Write a C function that prints some basic info about Python lists.

---

## Usage

1. Clone the repository:
   ```bash
	  git clone https://github.com/yourusername/alx-higher_level_programming.git
   ```
2. Navigate to the project directory:
```bash
cd 0x03-python-data_structures
```
Run Python test files:

```bash
python3 <main_test_file>.py
```
For C tasks, compile and run:

```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 <source_file>.c -o output
./output
```
