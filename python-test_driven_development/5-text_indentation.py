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
    string = text.replace('.', '.\n\n').replace(':', ':\n\n')\
        .replace('?', '?\n\n')
    for i in range(len(text)):
        string = string.replace('\n ', '\n')
    print(string, end='')
