#!/usr/bin/python3
"""
A module to  “base” of all other classes in this project.
The goal of it is to manage id attribute
 in all classes to avoid duplicating the same code.
 """

class Base:
    """
    Define the base class of all other classes

    Private Class Attributes:
        __nb_object (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the class consturctor

        Args:
        id (int): The identity of new base 
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
