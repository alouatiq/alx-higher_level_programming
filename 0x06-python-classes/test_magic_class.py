#!/usr/bin/python3
MagicClass = __import__('103-magic_class').MagicClass

# Create an instance of MagicClass with radius 5
mc = MagicClass(5)

# Test the area method
print("Area:", mc.area())  # Expected: 78.53981633974483

# Test the circumference method
print("Circumference:", mc.circumference())  # Expected: 31.41592653589793
