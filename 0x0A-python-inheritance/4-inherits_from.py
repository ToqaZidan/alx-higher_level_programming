#!/usr/bin/python3
"""Define a checking inheritance function"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Attributes:
    obj: The object to be  checked.
    a_class: The class to check against.

    Return:
    True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class,
        otherwise False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
