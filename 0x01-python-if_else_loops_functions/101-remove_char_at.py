#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for c in range(len(str)):
        if c != n:
            result += str[c]
    return result
