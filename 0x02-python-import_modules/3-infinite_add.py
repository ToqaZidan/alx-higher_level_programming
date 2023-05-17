#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all number of arguments."""
    import sys

    total = 0
    for j in range(len(sys.argv) - 1):
        total += int(sys.argv[j + 1])
    print("{}".format(total))
