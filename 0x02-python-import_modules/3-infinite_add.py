#!/usr/bin/python3

if __name__ == "__main__":
    """print the addition of all arguments."""
import sys
sum = 0
for i in range (1, len(sys.argv)):
    sum = sum + int(sys.argv[i])
print("{}".format(sum))

