# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 19:23:21 2019

"""

def Product(x, y):
    strx = str(x);
    maxVal = 0;
    maxz = []
    for i in list(range(len(strx) - y + 1 )):
        z = strx[0 + i:y + i]
        product = 1;
        for t in z:
            product = int(t) * product;
            if product > maxVal:
                maxVal = product;
                maxz = z
    return maxVal, maxz;