#!/usr/bin/python3
for int in range(100):
    if int == 99:
        print(int)
    else:
        print("{}".format('0' + str(int) if int < 10 else int), end=", ")
