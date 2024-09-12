# Python Import Modules

This project contains a series of Python scripts demonstrating various concepts related to importing modules and handling command-line arguments in Python.

## Table of Contents

1. [Description](#description)
2. [Files](#files)
3. [Requirements](#requirements)
4. [Usage](#usage)

## Description

This project is part of the ALX Higher Level Programming curriculum. It focuses on the following Python concepts:

- Importing functions from other files
- Using imported functions
- Creating modules
- Using the built-in function `dir()`
- Preventing code in your script from being executed when imported
- Using command line arguments with your Python programs

## Files

The repository contains the following Python scripts:

- `0-add.py`: Imports a simple function from a simple file
- `1-calculation.py`: Imports functions from a file and does some maths
- `2-args.py`: Prints the number of and the list of its arguments
- `3-infinite_add.py`: Prints the result of the addition of all arguments
- `4-hidden_discovery.py`: Prints all the names defined by a compiled module
- `5-variable_load.py`: Imports a variable from a file and prints its value
- `100-my_calculator.py`: Imports all functions from a file and handles basic operations
- `101-easy_print.py`: Prints #pythoniscool in the standard output
- `102-magic_calculation.py`: Python function that does exactly the same as a given Python bytecode
- `103-fast_alphabet.py`: Prints the alphabet in uppercase

## Requirements

- Python 3.8.5
- Ubuntu 20.04 LTS
- pycodestyle 2.8.*

## Usage

To run any of the scripts, use the following command format:

```
./script_name.py [arguments]
```

For example:

```
./0-add.py
./2-args.py Hello Welcome To The Best School
./3-infinite_add.py 1 2 3 4 5 6
./100-my_calculator.py 3 + 5
```

Note: Make sure to make the scripts executable using `chmod +x script_name.py` before running them.
