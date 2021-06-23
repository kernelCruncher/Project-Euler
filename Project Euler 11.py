# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:01:59 2019

"""

def readInGrid(x):
    a = [];
    f = open(x, "r");
    for line in f:
        line = line.rstrip('\n')
        line = list(map(int, line.split(" ")));
        a.append(line)
    return a;

def checkForLargestProduct(x):
    grid = readInGrid(x);
    noOfRows = len(grid);
    noOfColumns = len(grid[0]);
    maxSum = 0;
    for i in list(range(noOfRows)):
        for j in list(range(noOfColumns)):
            if noOfColumns - j >= 4 and grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3] > maxSum:
                    maxSum = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3];
            if noOfRows - i >=4 and grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j] > maxSum:
                    maxSum = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j];
            if noOfColumns - j >= 4 and noOfRows - i >=4 and grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3] > maxSum:
                    maxSum = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j];
            if  j >= 3 and noOfRows - i >=4 and grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3] > maxSum:
                    maxSum = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3];
    return maxSum
            
        