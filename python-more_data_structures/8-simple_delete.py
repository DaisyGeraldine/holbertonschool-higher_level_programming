#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # other form
    # for i in list(a_dictionary.keys()):
    #     if i == key:
    #         del a_dictionary[key]
    # return a_dictionary
    if a_dictionary.get(key):
        del a_dictionary[key]
    return a_dictionary
