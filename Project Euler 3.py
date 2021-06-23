# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:40:57 2019

"""

#The largest prime factor.
#Find prime factors
#Find factors

def factors(x):
    factors = []
    a = list(range(1,x+1))
    for candidate in a:
        if x % candidate ==0:
            factors.append(candidate)
    return factors


def primeFactors(x):
    primeFactors = []
    a = list(range(2,x+1))
    for candidate in a:
        if x % candidate == 0 and len(factors(candidate))==2:
            primeFactors.append(candidate)
    return primeFactors


def largestPrimeFactor(x):
    a = primeFactors(x)
    return max(a);


#The following is a recursive attempt.
def primeFactors2(x):
    if x==1:
        return [1];
    elif x== 2:
        return [2];
    else:
        primeFactors = []
        a = list(range(2,x+1))
        for candidate in a:
            if x % candidate == 0:
                if len(primeFactors2(candidate))==1:
                    primeFactors.append(candidate)
    return primeFactors            