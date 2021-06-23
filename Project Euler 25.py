# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 22:44:10 2019

"""

def Fibonacci(n):
    if n == 1:
        return 1;
    if n==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2);

#A quicker implementaion would be not to use the Fibonacci sequence.    
def FibonacciSeq(n):
    if n == 1:
        return 1;
    i = 2;
    maxTerm = 1;
    old2 = 1;
    old1 = 1; 
    while maxTerm < n:
        i+= 1;
        temp = old1 + old2
        maxTerm = len(str(temp));
        old2 = old1;
        old1 = temp;
    print(f"The {i}-th Fibonacci term, which has value {temp} is the first to have {n} digits.")
        
    