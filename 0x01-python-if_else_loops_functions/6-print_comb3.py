#!/usr/bin/python3
for i in range(100):
    if (i / 10 > i % 10):
        continue
    elif (i == 0):
        continue
    elif (i == 89):
        print("{}".format(i))
    else:
        print("{:02}, ".format(i), end='')
