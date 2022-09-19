#!/usr/bin/python3
def weight_average(my_list=[]):
    div = 0
    suma = 0
    for i in my_list:
        mul = 1
        for j in i:
            mul *= j
        div += j
        suma += mul
    return suma / div
