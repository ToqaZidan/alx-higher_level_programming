#!/usr/bin/python3
"""A Rectangle module base on super class Base"""
from model.Base import Base:


class Rectangle(Base):
    """Define a Rectangle class that inherites from `Base`."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x : The X coordinate of the rectangle.
        y : The Y coordinate of the rectangle.
        id : The identitt of the rectangle.

        Rasies:

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returns the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Get and set the width of the Rectangle

        Args:
            value (int): The height of the Rectangle.

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) != int:
                    raise TypeError("width must be an integer")
        if value <= 0:
                    raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
          Returns the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Get and set the height of the Rectangle

        Args:
            value (int): The height of the Rectangle.

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) != int:
                    raise TypeError("height must be an integer")
        if value <= 0:
                    raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
          Returns the X coordinate of the Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Get and set the X of the Rectangle

        Args:
            value (int): The height of the Rectangle.

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) != int:
                    raise TypeError("x must be an integer")
        if value <= 0:
                    raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Returns the y coordinate of the Rectangle

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Get and set the Y of the Rectangle

        Args:
            value (int): The Y coordinate of the Rectangle.

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) != int:
                    raise TypeError("y must be an integer")
        if value <= 0:
                    raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculate Area of Rectangle

        Return:
            The Area of Rectangle
        """
        return self.height * self.width
    
    def display(self):
        """

        print the Rectangle with defined sizes in `#`

        Returns:
        Rectangle print to the stdout.

        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

        def __str__(self):
           """
           Return the string representation of the rectangle.
           """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )
    

           
    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding the public method def update(self, *args)
        that assigns an argument to each attribute.

        1st argument:  id attribute
        2nd argument:  width attribute
        3rd argument:  height attribute
        4th argument:  x attribute
        5th argument:  y attribute
        """
        argc = len(args)
        kwargc = len(kwargs)
        update_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, update_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in update_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
