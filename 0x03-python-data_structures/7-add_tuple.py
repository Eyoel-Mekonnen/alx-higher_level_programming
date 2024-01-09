#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    if not isinstance(tuple_a, tuple):
        tuple_a = (tuple_a,)
    if not isinstance(tuple_b, tuple):
        tuple_b = (tuple_b,)
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if (len_a == 0 and len_b == 0):
        new_tuple = [0, 0]
        new_tuple = tuple(new_tuple)
        return new_tuple
    for i in range(0, 2):
        if (len_a > len_b and i >= len_b):
            new_tuple.append(tuple_a[i])
        elif (len_b > len_a and i >= len_a):
            new_tuple.append(tuple_b[i])
        else:
            if (i < len_a and i < len_b):
                new_tuple.append(tuple_a[i] + tuple_b[i])
            else:
                new_tuple.append(0)

    new_tuple = tuple(new_tuple)
    return new_tuple
