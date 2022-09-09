#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        cont = b
        for i in range(cont + 1):
            _pow = a ** cont
    else:
        cont = b * -1
        for i in range(cont + 1):
            _pow = 1 / a ** cont
    return _pow
