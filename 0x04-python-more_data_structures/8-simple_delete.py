#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """A function that deletes a key in a dictionary"""
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
