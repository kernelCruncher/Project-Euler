# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:06:51 2019

"""

#Calculate triangular number
#Calculate factors of triangular number
#Find first triangular number with n divisors.

def triangularNumber(x):
    sumOfNumbers = 0;
    for i in list(range(1,x+1)):
        sumOfNumbers += i;
    return sumOfNumbers;

def factors(x):
    factors = [];
    for i in list(range(1, x+1)):
        if x % i == 0:
            factors.append(i);
    return factors;

def nDivisors(x):
    maxDivisors = 1;
    i = 0;
    while maxDivisors <=  x:
        i +=1;
        maxDivisors = len(factors(triangularNumber(i)));
    print("The first triangular number to have over " + str(x) + " factors is the "+ str(i) + "-th and has value " + str(triangularNumber(i)));
            