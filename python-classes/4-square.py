#!/usr/bin/python3
"""Defines a Square class with size, area, and printing functionality."""


class Square:
    """Represents a square with size and methods to compute and print it."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size  # Triggers the setter for validation

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
