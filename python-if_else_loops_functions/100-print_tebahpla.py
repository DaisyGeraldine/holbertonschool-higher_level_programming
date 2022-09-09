#!/usr/bin/python3
for i in range(-122, -96):
    char = i * -1
    if i % 2 == 0:
        print('{}'.format(chr(char)), end="")
    else:
        print('{}'.format(chr(char - 32)), end="")
