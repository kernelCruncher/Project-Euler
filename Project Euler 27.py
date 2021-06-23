# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:37:20 2019

"""
#We can use that when n= 0, n^2 +an + b = b and thus will only be prime if b is prime.
#This immediately means that we can disregard thos evalues of b that are not prime.
#We can reduce this further by using the sieve of Eratosthenese to find only the values of b.

'''
import math

def Sieve(number):
    primes = []
    for i in range(2,number+1):
        primes.append(i)
    
    i = 2
    #from 2 to sqrt(number)
    while(i <= int(math.sqrt(number))):
        #if i is in list
        #then we gotta delete its multiples
        if i in primes:
            #j will give multiples of i,
            #starting from 2*i
            for j in list(range(i*2, number+1, i)):
                if j in primes:
                    #deleting the multiple if found in list
                    primes.remove(j)
        i = i+1
    return primes;'''
        
     
def IsPrime(x):
    for i in list(range(2, int(x/2) + 1)):
        if x % i == 0:
            return False;
    return True;

def f(x):
    primeMax = 0;
    prodAB = 0;
    aMax = 0;
    bMax = 0;
    for a in list(range(-x+1, x)):
        for b in list(range(2,x+1)):
            n = 0;
            primeCount = 0;
            while n**2 + a*n + b > 0 and IsPrime(n**2 + a*n + b):
                n += 1;
                primeCount += 1;
            if primeCount > primeMax:
                primeMax = primeCount;
                aMax = a;
                bMax = b;
                prodAB = a*b;
    return aMax, bMax, primeMax, prodAB;
                
                