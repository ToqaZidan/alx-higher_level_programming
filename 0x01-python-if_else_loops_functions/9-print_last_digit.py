#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lasTdig = number % 10
    else:
        lasTdig = number % -10
        lasTdig *= -1

    print("{:d}".format(lasTdig), end='')
    return (lasTdig)
