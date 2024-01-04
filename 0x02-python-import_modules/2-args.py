#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    if (len(sys.argv) == 1):
        print("{} arguments.".format(0))
    if (len(sys.argv) == 2):
        print("{} argument:".format(len(sys.argv) -1))
    elif (len(sys.argv) > 2):
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv)):
        if (i >= 1):
            print("{}: {}".format(i, sys.argv[i]))
