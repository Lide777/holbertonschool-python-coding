#!/usr/bin/python3
"""Defines a class Square with validated size attribute."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
