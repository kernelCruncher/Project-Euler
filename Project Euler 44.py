from ProjEuler45 import pentagonal

#Need to check sum and difference.

def proj44():
    i = 1;
    pentagonals = set()
    while True:
        a = pentagonal(i)
        for b in pentagonals:
            c = a - b
            if c in pentagonals:
                if abs(b - c) in pentagonals:
                    return abs(b - c)
        print(a)
        pentagonals.add(a)
        i+=1
            
