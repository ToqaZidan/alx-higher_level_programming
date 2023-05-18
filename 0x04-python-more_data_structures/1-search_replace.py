#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
        a function that replaces all occurrences
        of an element by another in a new list.

        @m: elements
    '''
    if len(my_list) == 0:
        return my_list

    new_lst = [m if m != search else replace for m in my_list]
    return new_lst
