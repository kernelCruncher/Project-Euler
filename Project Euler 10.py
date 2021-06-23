# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 08:42:55 2019

"""

import math

def SieveOfEratosthenes(n):
    primes = list(range(2, n + 1));
    i=2    
    while(i <= int(math.sqrt(n))):
        if i in primes:
            for j in list(range(i*2, n+1, i)):
                if j in primes:
                    primes.remove(j)
        i = i+1
    return primes;



def SumOfPrimes(n):
    primes = SieveOfEratosthenes(n);
    sumOfPrimes = 0;
    for i in primes:
        sumOfPrimes+=i;
    return sumOfPrimes;
                    
                