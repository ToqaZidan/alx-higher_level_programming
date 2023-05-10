#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) >= 97 and ord(str[x]) < 123:
            toconvert = 32
        else:
            toconvert = 0
        print("{:c}".format(ord(str[x]) - toconvert), end='')
    print()
