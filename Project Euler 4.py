# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:33:22 2019

"""

def palindromeCheck(x):
    reversedNumber = "";
    indices = list(range(1, len(str(x)) + 1))
    reversedIndices = [t * -1 for t in indices]
    for s in reversedIndices:
        reversedNumber += str(x)[s]
    return(reversedNumber == str(x))

#Alternative check using advanced slice
    
def palindromeCheckDiff(x):
    return str(x) == str(x)[::-1] 
    
def palindrome():
    maxValue = 1;
    for x in list(range(1, 1000)):
        for y in list(range(1,1000)):
            if palindromeCheck(x*y) and x*y > maxValue:
                maxValue = x * y;
    return maxValue