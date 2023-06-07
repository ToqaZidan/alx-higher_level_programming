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

    def area(self):
        """
        Calculate Area of Rectangle

        Return:
            The Area of Rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculare perimeter of Rectangle

        Return:
            Perimeter of Rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __print_rectangle(self):
        """

        Draw the Rectangle with defined sizes

        Returns:
            str_r: `Empty` If width or height == `0`,
            otherwise returns a string with the Rectangle.

        """

        str_r = ''
        width = self.__width
        height = self.__height

        if width == 0 or height == 0:
            return str_r

        for i in range(height):
            for j in range(width):
                str_r += '#'

            if i != height - 1:
                str_r += '\n'

        return str_r

    def __str__(self):
        """

        Returns a string with printable  representation of the Rectangle.

        """

        return self.__print_rectangle()
