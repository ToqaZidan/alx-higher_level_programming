#!/usr/bin/python3
"""Defines a Derived class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using Base class 'BaseGeometry'."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Attributes:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """ Return the string representation"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """retrurn the area of recatngle"""
        return self.__width * self.__height
