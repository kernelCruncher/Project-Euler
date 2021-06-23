# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:41:13 2019

"""

#The key is finding an upper bound.
#d is the maximum number of digits a number can have
#if there is any chance for the sum the fifth power of its digits will
#equal itself. 7 * 9**5 = 413343 which means that this is less than any seven
#digit number and thus there are at most 6 digits. 6 * 9**5
def f():
    listOfNumbers =[];
    sumUp = 0;
    for i in list(range(10, 354295)):
        sumDigit = 0;
        for char in str(i):
            sumDigit += int(char)**5;       
        if sumDigit == i:
            listOfNumbers.append(i);
            sumUp += i;
    return listOfNumbers, sumUp;