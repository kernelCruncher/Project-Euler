# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:22:47 2019

"""

def factorial(x):
    if x == 1:
        return 1;
    else:
        return x * factorial(x-1);
    
def sumFactorial(x):
    stringFac = str(factorial(x));
    sumFac = 0;
    for i in stringFac:
        sumFac += int(i);
    return sumFac;
        
    
        