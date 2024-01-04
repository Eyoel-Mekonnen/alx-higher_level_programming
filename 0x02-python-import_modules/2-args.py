#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    for i in range(len(sys.argv)):
        if (len(sys.argv) == 1):
            print("{} arguments".format(i))
            break
        if (i == 0):
            print("{} arguments".format(len(sys.argv) - 1))
        if (i >= 1):
            print("{}: {}".format(i, sys.argv[i]))
