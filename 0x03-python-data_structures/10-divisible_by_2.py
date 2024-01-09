#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_2 = []
    for i in range(0, len(my_list)):
        if (my_list[i] % 2 == 0):
            list_2.append(True)
        elif (my_list[i] % 2 != 0):
            list_2.append(False)
    return list_2
