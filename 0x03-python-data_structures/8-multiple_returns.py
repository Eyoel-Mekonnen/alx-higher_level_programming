#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == "" or sentence is None):
        return None
    tuple_list = []
    tuple_list.append(len(sentence))
    tuple_list.append(sentence[0])
    tuple_list = tuple(tuple_list)
    return tuple_list
