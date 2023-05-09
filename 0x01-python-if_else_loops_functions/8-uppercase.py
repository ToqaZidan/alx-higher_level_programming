#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if c.isalpha():
            result += "{:s}".format(chr(ord(c) - 32))
        else:
            result += c
    print("{:s}".format(result)
