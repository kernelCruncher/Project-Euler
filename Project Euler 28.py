# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:06:52 2019

"""

#Solve this using mathematics:
#Each corner has formula:
#n**2, n**2 - (n-1), n**2 -2(n-1), n**2 - 3(n-1) where n is odd.

def f(n):
    sumUp = 1;
    for i in list(range(3,n+1, 2)):
        sumUp += 4*i**2 - 6 *(i-1);
    return sumUp;
 
#Brute force approach

def g(n):
    M = []
    for i in list(range(n)):
        M.append([None] * n);
        x,y = n//2;
    for j in list(range(1, n+1, 2)):
        for k in list(range(j**2)):
            M[x][y] = 1;
    return M;