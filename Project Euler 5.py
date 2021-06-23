# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:12:49 2019

"""

def evenlyDivisible(x):
    s = 1;    
    while True:
        s+=1;
        for y in list(range(2,x+1)):
            if s %y == 0:
                if y == x:
                    return s;
                continue
            else:
                break        

##Alternative approach. It doesn't work.
def evenlyDivisibleNew(x):
    s = 1;    
    while True:
        s+=1;
        for y in list(range(2,x+1)):
            if s %y == 0:
                continue
            else:
                break    
            return s;
        