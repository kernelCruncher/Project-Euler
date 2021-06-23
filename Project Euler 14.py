# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:38:47 2019

"""
def OddCollatz(x):
    return 3 * x + 1;

def EvenCollatz(x):
    return x/2;
    
def CollatzSeq(x):
    if x%2 == 0:
        return EvenCollatz(x);
    return OddCollatz(x);

def CollatzProcess(n):
    maxTerms = 1;
    maxStartingNumber = 1;
    for i in list(range(2,n)):
        terms = 1
        x = i;
        while x > 1:
            x = CollatzSeq(x);
            terms += 1;
        if terms > maxTerms:
            maxTerms = terms;
            maxStartingNumber = i;
    print(f"Less than {n}, the starting number {maxStartingNumber} had the highest number of terms, which was {maxTerms}")
            
            