#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in range(len(a_dictionary)):
        print('{}: {}'.format(sorted(a_dictionary)[i],
                              a_dictionary[sorted(a_dictionary)[i]]))
