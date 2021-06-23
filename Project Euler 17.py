# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:06:52 2019

"""

import inflect
p = inflect.engine();

def NumberWordCount(x):
    wordNumber = p.number_to_words(x).replace(",","");
    return len(wordNumber.split(" "));

def CountAll(x):
    sumUp = 0;
    for number in list(range(1,x+1)):
        sumUp += NumberWordCount(number)
    return sumUp;