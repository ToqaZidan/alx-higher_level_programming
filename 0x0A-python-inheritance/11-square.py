#!/usr/bin/python3
"""Defines a Derived Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Attribute:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def __str__(self, size):
        """return string representation of square"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
