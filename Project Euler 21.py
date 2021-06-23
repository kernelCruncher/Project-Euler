# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 16:53:58 2019

"""

def divisors(x):
    divisors = [];
    for i in list(range(1,x)):
        if x % i == 0:
            divisors.append(i);
    return divisors;

def sumDivisors(x):
    sumDivisors = 0;
    for i in divisors(x):
        sumDivisors += i;
    return sumDivisors;

def amicablePairChecker(x):
    amicablePair = [];
    sumAm = 0;
    a = list(range(2,x));
    for i in a:
        b = sumDivisors(i)
        if i == sumDivisors(b) and i != b:
            amicablePair.append((i, b))
            sumAm+=(i+b)
            a.remove(b)     
    print(f"The sum of all amicable numbers less than {x} is { sumAm}");
    print(f"The pairs of all amicable numbers is{ amicablePair}");
        
        

        