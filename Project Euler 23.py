# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:17:25 2019

"""

def IsAbundant(x):
    sumUp = 0;
    for i in list(range(1,int(x/2) + 1)):
        if x % i == 0:
            sumUp += i;
    if x < sumUp:
        return True;
    else:
        False;
        
def CanBeExpressedAsTwoAbundant(x):
    for i in list(range(1,int(x/2) +1 )):
        if IsAbundant(i) and IsAbundant(x-i):
            return True
    return False;

def SumOfNumbersThatCannotBeExpressedAsSum(x):
    sumUp =0;
    for i in list(range(1,x+1)):
        if not CanBeExpressedAsTwoAbundant(i):
            sumUp += i;
    return sumUp;
        
        