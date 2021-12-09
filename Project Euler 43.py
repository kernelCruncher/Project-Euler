#Use Permutations to create the pandigital list. It will speed up the process.
def pandigList():
    pandigital = ['0']
    for i in range(1,10):
        temp = []
        for j in range(0,i+1):
            for element in pandigital:
                newElement = element[:j] + str(i) + element[j:]
                temp.append(newElement)
        pandigital = temp
    return pandigital

#Using List Comprehensions        
def pandigList2():
    pandigital = ['0']
    for i in range(1,10):
        pandigital = [element[:j] + str(i) + element[j:] for j in range(0,i+1) for element in pandigital] 
    return pandigital
        
        
def proj43():
    pandigList = [];
    primes = [2,3,5,7,11,13,17]
    for i in pandigList2():
        for j in range(1,8):
            sub = i[j:j+3]
            # print(sub)
            intSub = int(sub)
            if intSub % primes[j-1] != 0:
                break
            elif j==7:
                pandigList.append(int(i))
    return sum(pandigList)