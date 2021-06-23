# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:11:36 2019

"""

def f(a,b):
    c = [];
    for i in list(range(2,a+1)):
        for j in list(range(2,b+1)):
            d = i**j;
            if d not in c:
                c.append(d);
    c.sort();
    return c,len(c);