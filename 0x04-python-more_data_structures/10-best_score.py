#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sort_value = []
    for key in a_dictionary:
        sort_value.append(a_dictionary[key])
    sort_value.sort()
    max_value = sort_value[len(sort_value) - 1]
    for key in a_dictionary:
        if (a_dictionary[key] == max_value):
            return key
