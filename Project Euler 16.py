# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:01:49 2019

"""

def SumOfDigits(x):
    number = str(2**x);
    product = 0;
    for i in number:
        product += int(i);
    return product;            