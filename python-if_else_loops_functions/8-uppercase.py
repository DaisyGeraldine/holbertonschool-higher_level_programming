#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (ord(char) >= 97 and ord(char) <= 122):
            char_upper = ord(char) - 32
        else:
            char_upper = ord(char)
        print('{}'.format(chr(char_upper)), end="")
    print('{}'.format(""))
