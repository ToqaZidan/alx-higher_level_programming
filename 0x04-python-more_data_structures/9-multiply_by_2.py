#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary with
    all values multiplied by 2
    """
    NewDir = a_dictionary.copy()
    listkeys = list(NewDir.keys())

    for i in listkeys:
        NewDir[i] *= 2

    return (NewDir)
