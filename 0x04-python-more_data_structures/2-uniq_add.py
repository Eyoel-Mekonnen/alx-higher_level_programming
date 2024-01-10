#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in range(0, len(my_list)):
        tracker = -1
        for j in range(i + 1, len(my_list)):
            if (my_list[i] == my_list[j]):
                tracker = tracker + 1
        if (tracker == -1):
            sum = sum + my_list[i]
    return sum
