#!/usr/bin/python3
"""Defines a class Rectangle with width, height, area, perimeter,
string representation, eval, custom deletion message, and instance counting."""


class Rectangle:
    """Represents a rectangle with width and height."""

    # Public class attribute to count the number of instances.
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either
            width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle using '#'.

        Returns:
            str: A string representation of the rectangle, or an empty
            string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a string representation that can recreate the object.

        Returns:
            str: A string representation of the rectangle that can be
            used with eval() to create a new instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted
        and decrement the instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
