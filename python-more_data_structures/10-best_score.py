#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best_value = 0
    for i, v in enumerate(list(a_dictionary)):
        if a_dictionary[v] > best_value:
            best_value = a_dictionary[v]
            student = v
    return student
