#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module 5-text_indentation
   Created on Sunday, September 25, 2022
   @author: Daisy Chipana Lapa
"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each of
       these characters: ., ? and :
        Args:
             text: must be a string
        Returns:
             prints a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print('{}'.format(text[i]), end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            i += 1
            print("\n")
        i += 1
