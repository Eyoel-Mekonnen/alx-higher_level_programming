#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tmp = number
if (tmp < 0):
    tmp = tmp * -1
if (number < 0):
    print(f"Last digit of {number} is -{tmp % 10} and is less than 6 and not 0")
elif (tmp % 10 > 5):
    print(f"Last digit of {number} is {tmp % 10} and is greater than 5")
elif (tmp % 10 == 0):
    print(f"Last of {number} is {tmp % 10} and is 0")
elif (tmp % 10 < 6 ):
    print(f"Last of {number} is {tmp % 10} and is less than 6 and not 0")
