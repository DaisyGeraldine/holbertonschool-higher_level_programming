#!/usr/bin/python3
"""Task 11 : Square #2 """


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout """
    with open(filename) as f:
        for line in f:
            print(line, end="")
