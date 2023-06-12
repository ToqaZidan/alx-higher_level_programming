#!/usr/bin/python3
"""Integer validator module"""


class BaseGeometry:
    "Class BaseGeometry which is empty base class"

    def area(self):
        """Not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks a integer value

        Args:
            name (str): The name of the value.
            value (int): The value.

        Raises:
            TypeError: If `value` isn't a integer.
            ValueError: If `value` is <= 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
