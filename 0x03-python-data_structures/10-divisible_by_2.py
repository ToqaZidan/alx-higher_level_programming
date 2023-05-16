#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            list.append(True)
        else:
            list.append(False)
    return list
