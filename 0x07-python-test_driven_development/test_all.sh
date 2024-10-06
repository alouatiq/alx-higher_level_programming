#!/bin/bash

echo "Running main tests..."

# Test for Task 0: Integers Addition
echo "Testing 0-main.py (Integers Addition)"
./0-main.py
echo ""

# Test for Task 1: Matrix Division
echo "Testing 2-main.py (Matrix Division)"
./2-main.py
echo ""

# Test for Task 2: Say My Name
echo "Testing 3-main.py (Say My Name)"
./3-main.py
echo ""

# Test for Task 3: Print Square
echo "Testing 4-main.py (Print Square)"
./4-main.py
echo ""

# Test for Task 4: Text Indentation
echo "Testing 5-main.py (Text Indentation)"
./5-main.py
echo ""

# Test for Task 5: Max Integer - Unittest
echo "Testing 6-main.py (Max Integer)"
./6-main.py
echo ""

# Test for Task 6: Matrix Multiplication
echo "Testing 100-main.py (Matrix Multiplication)"
./100-main.py
echo ""

# Test for Task 7: Lazy Matrix Multiplication using NumPy
echo "Testing 101-main.py (Lazy Matrix Multiplication)"
./101-main.py
echo ""

# Test for Task 8: CPython #3: Python Strings
echo "Testing 102-tests.py (CPython Strings)"
python3 102-tests.py
echo ""

# Now running doctests and unittests
echo "Running doctests..."
python3 -m doctest -v ./tests/*.txt

echo "Running unittests..."
python3 -m unittest discover tests

echo "All tests completed!"
