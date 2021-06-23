# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:51:34 2019

"""

def GiveMaxNumber(x):
    if len(x) == 1:
          return str(x[0]);
    y = [];
    for i in x:
        newx = x[:];
        newx.remove(i);
        for j in GiveMaxNumber(newx):
            y.append(str(i) + j);
    return y;

def Prob3(x):
    y = list(range(0,x+1));
    return GiveMaxNumber(y)

#This is to get a specific entry in the sequence
def GetTerm(n, term):
    return Prob3(n)[term - 1];
    
        