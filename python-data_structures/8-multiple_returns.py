#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        one_char = None
    else:
        one_char = sentence[0]
    len_str = len(sentence)
    return(len_str, one_char)
