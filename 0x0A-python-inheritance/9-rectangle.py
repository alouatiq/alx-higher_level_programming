#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry with area and str methods."""
    
    def __init__(self, width, height):
        """Initializes width and height, validating them as positive integers."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height
    
    def __str__(self):
        """Returns a formatted string description of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
