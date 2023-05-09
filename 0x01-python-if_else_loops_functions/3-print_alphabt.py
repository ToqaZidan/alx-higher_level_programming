#!/usr/bin/python3
for i in range(97, 97+26):
    if (i != ord('q')) & (i != ord('e')):
        print("{}".format(chr(i)), end="")
