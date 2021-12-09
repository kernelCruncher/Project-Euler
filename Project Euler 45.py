#Sets are one of the 4 built-in ways to store data in Python.
#The others are dictionary, list, tuple.

def triangular(n):
    return int(n*(n+1)/2);

def pentagonal(n):
    return int(n*(3*n -1)/2);

def hexagonal(n):
    return int(n*(2*n-1));

def proj45():
    i = 2;
    triangulars = set()
    pentagonals = set()
    hexagonals = set()
    while True:
        triangulars.add(triangular(i))
        pentagonals.add(pentagonal(i))
        hexagonals.add(hexagonal(i))
        if (len(triangulars.intersection(pentagonals,hexagonals))>1):
            print(triangulars.intersection(pentagonals,hexagonals))
            break;
        i+=1
        continue
#1533776805