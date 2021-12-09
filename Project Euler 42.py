def proj42():
    triangular = [n*(n+1) //2 for n in range(1,1000)]
    f = open("words2.txt", "r").read().lower()
    words = f.replace('"','').split(",")
    triangularWords = []
    for word in words:
        sumWords = 0;
        for x in word:
            ord(x)-96
            sumWords += (ord(x)-96)
        if sumWords in triangular:
            triangularWords.append(word)
    return triangularWords           