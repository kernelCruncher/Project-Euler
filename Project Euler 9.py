# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:39:12 2019

"""

def PythagTriplet():
    for a in list(range(1, 1000//3)):
        for b in list (range(a, 1000//2)):
           c = 1000 - a - b;
           if a**2 + b**2 == c**2:
               print("The numbers are:", [a,b,c], "The product is", a * b * c);
                    