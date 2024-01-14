#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    max_item = len(my_list)
    new_list = sorted(my_list)
    for item in range(max_item):
        print(new_list[item])
        if item + 1 < max_item:
            if new_list[item] != new_list[item + 1]:
                sum += new_list[item]
    return sum
