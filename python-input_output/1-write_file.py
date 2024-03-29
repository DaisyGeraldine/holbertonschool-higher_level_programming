#!/usr/bin/python3
"""Task 1 : Write to a file """


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
       and returns the number of characters"""
    with open(filename, 'w', encoding="utf-8") as f:
        characters = f.write(text)
        return characters
