# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:25:57 2019

"""

def SumOfSquares(x):
    sum = 0;
    for y in list(range(1,x+1)):
        sum += y**2;
        
    return sum;

def SquareOfSums(x):
    sum = 0;
    for y in list(range(1,x+1)):
        sum += y;
    return sum**2;

def Difference(x):
    return SquareOfSums(x) - SumOfSquares(x);