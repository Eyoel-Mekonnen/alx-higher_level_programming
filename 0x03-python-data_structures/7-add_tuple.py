#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a > len_b:
        length = len_a
    elif len_a == len_b:
        length = len_a
    else:
        length = len_b
    for i in range(0, length):
        if (len_a > len_b and i >= len_b):
            new_tuple.append(tuple_a[i])
        elif (len_b > len_a and i >= len_a):
            new_tuple.append(tuple_b[i])
        else:
            new_tuple.append(tuple_a[i] + tuple_b[i])
    new_tuple = tuple(new_tuple)
    return new_tuple
