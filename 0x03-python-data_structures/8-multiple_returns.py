#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_list =[]
    if (len(sentence) == 0):
        tuple_list.append(0)
        tuple_list.append("None")
        tuple_list = tuple(tuple_list)
        return tuple_list
    tuple_list.append(len(sentence))
    tuple_list.append(sentence[0])
    tuple_list = tuple(tuple_list)
    return tuple_list
