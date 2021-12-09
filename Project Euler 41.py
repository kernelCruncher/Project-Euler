from ProjEuler43 import pandigList2
from ProjEuler47 import isPrime
  
def projEuler41():
    a = [int(x)  for x in pandigList2() if isPrime(int(x))]
    return max(a)

def eratosthenes(n):
    multiples = []
    primes = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return primes

def projEuler41Alt():
    panDig = [prime for prime in eratosthenes(9876543210) if len(str(prime)) == set(str(prime))]
    return max(panDig)