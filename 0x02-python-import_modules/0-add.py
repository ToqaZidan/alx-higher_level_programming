#!/usr/bin/python3

if __name__ == "__main__":
    """
    Print the sum of two variables
    a=1 and b=2.
    """
    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
