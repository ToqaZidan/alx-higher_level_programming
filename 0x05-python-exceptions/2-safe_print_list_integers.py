#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    real_num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            real_num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (real_num)
