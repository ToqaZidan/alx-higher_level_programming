#!/usr/bin/python3
"""A function that adds all unique integers in a list"""

def uniq_add(my_list=[]):
    list = set(my_list)
    nom = 0

    for i in list:
        nom += i

    return (nom)
