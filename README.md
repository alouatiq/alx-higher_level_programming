# 0x00. Python - Hello, World

This project is your introduction to Python programming. It covers the basics of Python, printing, string manipulation, and cycle detection in linked lists using C. Below is a breakdown of all the tasks and the files associated with them, along with a brief description of each file's purpose.

## Table of Contents

- [Requirements](#requirements)
- [Tasks and Files](#tasks-and-files)
  - [0. Run Python file](#0-run-python-file)
  - [1. Run inline](#1-run-inline)
  - [2. Hello, print](#2-hello-print)
  - [3. Print integer](#3-print-integer)
  - [4. Print float](#4-print-float)
  - [5. Print string](#5-print-string)
  - [6. Play with strings](#6-play-with-strings)
  - [7. Copy - Cut - Paste](#7-copy---cut---paste)
  - [8. Create a new sentence](#8-create-a-new-sentence)
  - [9. Easter Egg](#9-easter-egg)
  - [10. Linked list cycle](#10-linked-list-cycle)
  - [11. Hello, write](#11-hello-write)
  - [12. Compile](#12-compile)
  - [13. ByteCode -> Python #1](#13-bytecode---python-1)

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All Python files must be executable and end with a new line.
- Python files must be interpreted/compiled with `python3` (version 3.8.5).
- Your Python scripts should use `pycodestyle` (version 2.8.*).
- All C files must be compiled with `gcc` using the flags `-Wall -Werror -Wextra -pedantic -std=gnu89`.
- All header files must be include guarded.

---

## Tasks and Files

### 0. Run Python file

**File**: `0-run`

**Task Description**: 
- Write a shell script that runs a Python script whose filename is saved in the environment variable `$PYFILE`.
  
**What the File Does**:
- The script simply executes the Python script pointed to by `$PYFILE` using `python3`.

---

### 1. Run inline

**File**: `1-run_inline`

**Task Description**: 
- Write a shell script that runs Python code stored in the environment variable `$PYCODE`.

**What the File Does**:
- It runs inline Python code stored in `$PYCODE` using the `-c` option of the `python3` command.

---

### 2. Hello, print

**File**: `2-print.py`

**Task Description**: 
- Write a Python script that prints exactly:
```
"Programming is like building a multilingual puzzle"
```


**What the File Does**:
- The script prints the exact string as specified using the `print()` function.

---

### 3. Print integer

**File**: `3-print_number.py`

**Task Description**: 
- Complete a Python script that prints the integer stored in the variable `number`, followed by the string `Battery street`.

**What the File Does**:
- Uses an f-string to correctly print an integer along with the string.

---

### 4. Print float

**File**: `4-print_float.py`

**Task Description**: 
- Complete a Python script that prints the float stored in the variable `number` with a precision of 2 digits.

**What the File Does**:
- Uses an f-string with formatting to display the float with exactly two decimal places.

---

### 5. Print string

**File**: `5-print_string.py`

**Task Description**: 
- Write a Python script that prints a string stored in the variable `str` three times, followed by its first 9 characters.

**What the File Does**:
- Concatenates the string three times and prints it, followed by a new line with only the first 9 characters of the string.

---

### 6. Play with strings

**File**: `6-concat.py`

**Task Description**: 
- Write a Python script that concatenates two strings and prints:
  ```
  Welcome to Holberton School!
  ```


**What the File Does**:
- Concatenates two strings (`str1` and `str2`) and prints the final output.

---

### 7. Copy - Cut - Paste

**File**: `7-edges.py`

**Task Description**: 
- Write a Python script that manipulates a string and prints:
- The first 3 letters of the string.
- The last 2 letters of the string.
- The middle part of the string.

**What the File Does**:
- Uses slicing to extract different parts of the string and prints them accordingly.

---

### 8. Create a new sentence

**File**: `8-concat_edges.py`

**Task Description**: 
- Complete the Python script to print:

```
object-oriented programming with Python
```


**What the File Does**:
- Uses string slicing to create the required sentence from the provided string.

---

### 9. Easter Egg

**File**: `9-easter_egg.py`

**Task Description**: 
- Write a Python script that prints “The Zen of Python” by Tim Peters.

**What the File Does**:
- Prints the Zen of Python by importing the `this` module.

---

### 10. Linked list cycle

**Files**:
- `lists.h`
- `10-check_cycle.c`

**Task Description**: 
- Write a function in C that checks if a singly linked list has a cycle in it.

**What the Files Do**:
- `lists.h`: Defines the structure of a singly linked list and declares function prototypes.
- `10-check_cycle.c`: Implements Floyd’s Cycle Detection Algorithm (Tortoise and Hare) to detect if a cycle exists in the linked list.

---

### 11. Hello, write

**File**: `100-write.py`

**Task Description**: 
- Write a Python script that prints exactly:

```
and that piece of art is useful - Dora Korpar, 2015-10-19
```
to the standard error.

**What the File Does**:
- Uses `sys.stderr.write()` to output the string to standard error and exits with status code `1`.

---

### 12. Compile

**File**: `101-compile`

**Task Description**: 
- Write a shell script that compiles a Python script file and outputs the bytecode file.

**What the File Does**:
- Compiles a Python script into bytecode using the `py_compile` module.

---

### 13. ByteCode -> Python #1

**File**: `102-magic_calculation.py`

**Task Description**: 
- Write a Python function `magic_calculation(a, b)` that does the same as the provided Python bytecode.

**What the File Does**:
- Implements the logic from the given bytecode to match its behavior.

---

## Conclusion

This project introduces the basics of Python programming and linked list cycle detection in C. By completing these tasks, you'll gain foundational knowledge in both Python and C while developing efficient algorithms.

