#!/bin/usr/python3
"""
A module that prints a list in sorted order
"""


class MyList(list):
    """
    Initialize Dervied class
    """

    def print_sorted(self):
        """
        Sort a list and print it
        """

        if issubclass(MyList, list):
            print(sorted(self))

