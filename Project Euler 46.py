from ProjEuler47 import isPrime
from math import sqrt

def check(primes, squares, n):
    for i in primes:
        for j in squares:
            if i + 2*j == n:
                return True
            continue;
    return False

    
def isSquare(x):
    root = sqrt(x)
    return int(root + 0.5) ** 2 == x

        
def proj46():
    i = 2;
    primes = [];
    squares = [1];
    while True:
        if isSquare(i):
            squares.append(i)
        if isPrime(i):
            primes.append(i)
        else:
            if (i%2 ==0): 
                pass
            elif check(primes, squares, i):
                pass;
            else:
                break
        i+=1
    return i
 #5777      