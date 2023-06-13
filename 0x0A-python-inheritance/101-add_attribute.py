#!/usr/bin/python3
"""A module for adding new attribute to an object"""
def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Attributs:
        obj: The object to which the attribute will be added.
        attr: The name of the attribute.
        value: The value to be assigned to the attribute.

    Raises:
        TypeError: If the object already has the attribute.
    """
    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
