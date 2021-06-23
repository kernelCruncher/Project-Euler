# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 20:19:39 2019

"""

from string import ascii_uppercase
LETTERS = {letter: index for index, letter in enumerate(ascii_uppercase, start=1)} 

def CalculateNames():
    names = open("p022_names.txt");
    line = names.readline();
    line = line.replace('"','' );
    splitLine = line.split(",");
    splitLine.sort();
    
    sumNames = 0;
    for name in splitLine:
        sumName = 0;
        for letter in name:
            sumName += LETTERS[letter];
        sumNames += sumName;
    return sumNames