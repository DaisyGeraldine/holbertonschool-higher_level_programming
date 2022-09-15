#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list[:]
    new_list = set(new_list)
    sum = 0
    for i in new_list:
        sum += int(i)
    return sum
