#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    a function that prints a dictionary by ordered keys.
    """
    ListOrder = list(a_dictionary.keys())
    ListOrder.sort()
    for i in ListOrder:
        print("{}: {}".format(i, a_dictionary.get(i)))
