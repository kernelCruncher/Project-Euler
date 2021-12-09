def isPrime(x):
    factors = []
    for y in range(2, x+1):
        if x%y == 0:
            factors.append(y)
    if len(factors) == 1:
        return True
    else:
        return False

def primeFactors(x):
    factors = []
    for y in range(2, x+1):
        if x%y ==0 and isPrime(y):
            factors.append(y)
    return factors

def twoPrimes():
    i =2;
    prevFactors = []
    while True:
       a = primeFactors(i)
       if len(a) == len(prevFactors) == 2:
           break;
       else:
           print(i, a)
           prevFactors = a;
           i += 1
    return i -1, i;


def threePrimes():
    i =3;
    prevFactors1 = []
    prevFactors2 = []
    while True:
       a = primeFactors(i)
       print(i, a)
       if len(a) == len(prevFactors1) == len(prevFactors2) == 3:
           break;
       else:
           prevFactors2 = prevFactors1;
           prevFactors1 = a
           i += 1
    return i-2, i -1, i;
 
       
def fourPrimes():
    i = 4;
    prevFactors1 = []
    prevFactors2 = []
    prevFactors3 = []
    while True:
       a = primeFactors(i)
       print(i, a)
       if len(a) == len(prevFactors1) == len(prevFactors2) == len(prevFactors3)  == 4:
           break;
       else:
           prevFactors3 = prevFactors2;
           prevFactors2 = prevFactors1;
           prevFactors1 = a
           i += 1
    return i-3, i-2, i -1, i;
# 134043 [3, 7, 13, 491]
# 134044 [2, 23, 31, 47]
# 134045 [5, 17, 19, 83]
# 134046 [2, 3, 11, 677]

#This should work for any n.
def nPrimes(n):
    dic = {}
    for i in range(1,n):
        dic[i] = [];
    j = n;
    while True:
       a = primeFactors(j)
       print(j, a)
       truth = True & (len(a) == n)
       for i in range(1,n):
           truth = truth & (n == len(dic[i]))
       if truth:
           break;
       else:
           for i in range(1,n-1):
               dic[i] = dic[i+1]
           dic[n-1] = a
           j += 1