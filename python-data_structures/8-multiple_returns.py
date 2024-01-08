#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_c = None
    else:
        first_c = sentence[0]
    len_str = len(sentence)
    return(len_str, first_c)
