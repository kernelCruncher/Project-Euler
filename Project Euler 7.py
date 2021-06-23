# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:38:18 2019

"""

def PrimeChecker(x):
    if x ==1:
        return False;
    elif x == 2:
        return True;
    else:
        for i in list(range(2,int(x/2) +1)):
            if x % i == 0:
                return False
        return True;

def PrimeCounter(n):
    x = 0;
    i = 0;
    while x < n:
        i+=1;
        if PrimeChecker(i) == True:
            x+=1
    return i;
            