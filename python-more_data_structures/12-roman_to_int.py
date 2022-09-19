#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) != True or roman_string is None:
        return 0
    suma = 0
    # string counter according to condition of the next character
    count = 1
    # count of string characters
    i = 0
    string = ''.join(reversed(roman_string))
    table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    while i < len(string):
        #count += 1
        if count < len(string):
            if table[string[i]] > table[string[i + 1]]:
                suma += (-1 * table[string[i + 1]]) + table[string[i]]
                i += 1
                count += 1
            else:
                suma += table[string[i]]
        else:
            if count == len(string):
                suma += table[string[i]]
        count += 1
        i += 1
    return suma
