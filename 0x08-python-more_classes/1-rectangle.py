#!/usr/bin/python3

""" Define a rectangle module """


class Rectangle:
    """
    Intialize a rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__check_width(width)
        self.__check_height(height)

        self.width = width
        self.height = height

    @property
    def width(self):
        """

        Returns the width of the Rectangle

        """

        return self.__width

    @width.setter
    def width(self, value):
        """

        get and set the size of the Rectangle

        Args:
            value (int): The width of the Rectangle.

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.

        """

        self.__check_width(value)
        self.__width = value

    @property
    def height(self):
        """

        Returns the width of the Rectangle

        """

        return self.__height

    @height.setter
    def height(self, value):
        """

        get and set the size of the Rectangle

        Args:
            value (int): The height of the Rectangle.

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.

        """

        self.__check_height(value)
        self.__height = value

    def __check_width(self, width):
        """

        Checks if the width is an integer

        Args:
            width (int): The width of the Rectangle.

        Raises:
            TypeError: If `width` type is not `intger`.
            ValueError: If `width` is less than `0`.

        """

        if self.__check_int(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive(width) is False:
            raise ValueError('width must be >= 0')

    def __check_height(self, height):
        """

        Checks if the height is a valid integer

        Args:
            height (int): The height of the Rectangle.

        Raises:
            TypeError: If `height` type is not `int`.
            ValueError: If `height` is less than `0`.

        """

        if self.__check_int(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int(self, value):
        """

        Checks if the value is an integer

        Args:
            value (int): The number to be checked

        Returns:
            int: If is a int `True`, `False` otherwise.

        """

        if type(value) is int:
            return True

        return False

    def __check_positive(self, value):
        """

        Checks if the value is a positive integer

        Args:
            value (int): The number to be checked

        Returns:
            int: `True` If value is >= 0, `False` otherwise.

        """

        if value >= 0:
            return True

        return False