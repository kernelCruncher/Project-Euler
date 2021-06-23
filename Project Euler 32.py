# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:02:48 2020

"""
# Quick check. We nkow products have to be at least 2 x 3 to give 4.
# We need to think of what combination our products will be.

def Splitter(x):
    word = [];
    for letter in x:
        word.append(letter);
    return word;
        

def Prob32():
    total = [];
    for j in list(range(1000,9999)): 
        for i in list(range(1, 10)):
            a = [];
            a.extend(Splitter(str(i)));
            a.extend(Splitter(str(j)));
            a.extend(Splitter(str(i*j)));
            if len(set(a)) == 9 and len(a) == 9:
                total.append(i*j);
    
    for j in list(range(100,999)): 
        for i in list(range(10, 99)):
            a = [];
            a.extend(Splitter(str(i)));
            a.extend(Splitter(str(j)));
            a.extend(Splitter(str(i*j)));
            if len(set(a)) == 9 and len(a) == 9:
                total.append(i*j);
    product = 1;
    for number in set(total):
        product = product * number; 
                
    return set(total), product;
                    