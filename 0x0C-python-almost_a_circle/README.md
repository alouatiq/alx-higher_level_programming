# 0x0C. Python - Almost a Circle

## Overview

The **'0x0C. Python - Almost a Circle'** project focuses on advanced Python object-oriented programming (OOP). You will implement and explore several OOP concepts like classes, inheritance, encapsulation, and more. This project will also teach you how to use JSON for serialization and deserialization of objects, which is essential for real-world applications. Additionally, you’ll write unit tests for the various methods and functionalities you implement. The project prepares you for larger Python projects, including the AirBnB clone project.

## Learning Objectives

At the end of this project, you should be able to explain the following concepts without help:

### General
- What is Unit testing, and how to implement it in a large project.
- How to serialize and deserialize a Class.
- How to write and read a JSON file.
- What is `*args` and `**kwargs` and how to use them.
- How to handle named arguments in a function.

## Project Structure

The project is divided into the following files and directories:

```
alx-higher_level_programming/            # Main repository
└── 0x0C-python-almost_a_circle/         # Project directory
    ├── README.md                        # Project documentation
    ├── models/                          # Directory for model classes
    │   ├── __init__.py                  # Makes 'models' a Python package
    │   ├── base.py                      # Base class implementation
    │   ├── rectangle.py                 # Rectangle class implementation
    │   └── square.py                    # Square class implementation
    ├── tests/                           # Directory for unit tests
    │   ├── __init__.py                  # Makes 'tests' a Python package
    │   ├── test_models/                 # Subdirectory for model-specific tests
    │   │   ├── __init__.py              # Makes 'test_models' a package
    │   │   ├── test_base.py             # Unit tests for Base class
    │   │   ├── test_rectangle.py        # Unit tests for Rectangle class
    │   │   └── test_square.py           # Unit tests for Square class
    ├── 0-main.py                        # Test file for Base class
    ├── 1-main.py                        # Test file for Rectangle class
    ├── 2-main.py                        # Test file for Rectangle attribute validation
    ├── 3-main.py                        # Test file for Rectangle area method
    ├── 4-main.py                        # Test file for Rectangle display method
    ├── 5-main.py                        # Test file for Rectangle __str__ method
    ├── 6-main.py                        # Test file for Rectangle display with x and y
    ├── 7-main.py                        # Test file for Rectangle update with *args
    ├── 8-main.py                        # Test file for Rectangle update with *args and **kwargs
    ├── 9-main.py                        # Test file for Square class
    ├── 10-main.py                       # Test file for Square size getter/setter
    ├── 11-main.py                       # Test file for Square update with *args and **kwargs
    ├── 12-main.py                       # Test file for Rectangle to dictionary representation
    ├── 13-main.py                       # Test file for Square to dictionary representation
    ├── 14-main.py                       # Test file for JSON string conversion
    ├── 15-main.py                       # Test file for saving JSON to file
```

### Classes

#### Base Class (`models/base.py`)
- Manages the `id` attribute in all future classes and handles JSON serialization and deserialization.

#### Rectangle Class (`models/rectangle.py`)
- Inherits from `Base` and adds `width`, `height`, `x`, and `y` attributes.
- Includes methods like `area()`, `display()`, and `update()`.

#### Square Class (`models/square.py`)
- Inherits from `Rectangle`.
- Represents a square, which is a special case of a rectangle where `width` equals `height`.

### Tests

The project follows Test-Driven Development (TDD). Unit tests for each class and method can be found in the `tests/test_models/` directory.

You can run all tests using the command:

```bash
python3 -m unittest discover tests
```

### Tasks

- **Task 0**: Implement unit tests for all classes and methods.
- **Task 1**: Create a `Base` class to manage the `id` attribute.
- **Task 2**: Implement a `Rectangle` class inheriting from `Base`.
- **Task 3**: Add attribute validation in `Rectangle` (e.g., `width` must be an integer greater than 0).
- **Task 4**: Implement methods like `area()` and `display()` in `Rectangle`.
- **Task 5**: Override the `__str__` method for better object representation.
- **Task 6**: Implement the `Square` class inheriting from `Rectangle`.
- **Task 7**: Add `update()` methods with `*args` and `**kwargs`.
- **Advanced Tasks**: Implement JSON serialization, deserialization, and saving to file.

### How to Run

To execute the project, you can manually run the test files provided (`0-main.py`, `1-main.py`, etc.), or you can run the unit tests.

For example, to run the `0-main.py` script:

```bash
$ python3 0-main.py
```

To run the unit tests:

```bash
$ python3 -m unittest discover tests
```

# Resources

Python args/kwargs
JSON encoder and decoder
unittest module
Python test cheatsheet

Author
AL OUATIQ H.
