# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:54:23 2019

"""

#This requires some mathematical concepts.
#Think about it: in an nxn grid, we must always go right n times
#and down n-times in order to go from top left to bottom right. The only difference is
#the order of Ds and Rs, i.e. DDRR, DRDR, etc. This is a permutation problem
# as the order matters. The number of different permutations of n objects of
# which n1 are of one kind, n2 are of a second kind: 

import math;

def CalculateLatticePaths(x):
    return math.factorial(2*x)//(math.factorial(x) ** 2);

#Here is a recursive approach:
def recPath(gridSize):
    # base case, no moves left
    if gridSize == [0,0]: return 1
    # recursive calls
    paths = 0
    # move left when possible
    if gridSize[0] > 0:
        paths += recPath([gridSize[0]-1,gridSize[1]])
    # move down when possible
    if gridSize[1] > 0:
        paths += recPath([gridSize[0],gridSize[1]-1])
    return paths


#Dynamic Programming:
def route_num(grid_size):
    L = [1] * grid_size
    for i in list(range(grid_size)):
        for j in list(range(i)):
            L[j] = L[j] + L[j-1]
        L[i] = 2 * L[i - 1]
    return L[grid_size - 1]