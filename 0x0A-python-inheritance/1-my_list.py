#!/usr/bin/python3
"""
A module that prints a list in sorted order
"""


class MyList(list):
    """
    Initialize Derived class
    """

    def print_sorted(self):
        """
        A function that sort a list and print it
        """
        print(sorted(self))
