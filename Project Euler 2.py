# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:26:48 2019

"""

def Fibonacci(n):
    if n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2) 
 
#The following computes the sum of the  nth terms in the Fibonacci sequence where n is even.   
def CreateFibonacciListOld():
    fibSum = 1;
    fib = [0,1];
    while fib[-1] + fib[-2] < 4000000:
        fib.append(fib[-1] + fib[-2]);
        if len(fib) %2 ==0:
           fibSum += fib[len(fib) -1]
    return fibSum;

#The following computes the sum of the non-even terms in te Fibonacci sequence.   
def CreateFibonacciList():
    fibSum = 2;
    fib1 = 1; fib2 = 2;
    while fib1 + fib2 < 4000000:
        fib1 = fib2
        fib2 = fib1 + fib2
        if fib2 %2 == 0:
           fibSum += fib2;
    return fibSum

CreateFibonacciList();

