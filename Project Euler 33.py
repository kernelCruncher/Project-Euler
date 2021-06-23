# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:16:40 2020

"""

def noSame(x,y):
    strx = str(x);
    stry = str(y);
    return (strx[0] not in stry and strx[1] not in stry) or ("0" in strx or "0" in stry);

def removeNo(x,y):
    strx = str(x);
    stry = str(y);
    for i in strx:
        if i in stry:
           newx = int(strx.replace(i,"",1));
           newy = int(stry.replace(i,"",1));
           return newx, newy;
       
def gcd(x,y):
    gcd = 1;
    for i in list(range(2,x+1)):
        if x%i == 0 and y%i == 0 and i > gcd:
            gcd = i;
    return gcd;

def Prob33():
    panDigitalNum = [];
    panDigitalDenom = [];
    panDigital = [];
    product = 1;
    for x in list(range(10,100)):
        for y in list(range(x + 1,100)):
            if noSame(x,y):
                continue;
            a,b = removeNo(x,y);
            if x/y == a/b:
                panDigitalNum.append(a);
                panDigitalDenom.append(b);
                panDigital.append(str(x)+"/"+str(y))
                product = product * (a/b);
    
    prodNum = 1;
    prodDenom = 1;
    for i in list(range(len(panDigitalNum))):
        prodNum = prodNum * panDigitalNum[i];
        prodDenom = prodDenom * panDigitalDenom[i];
    Denomgcd = gcd(prodNum, prodDenom)
    return panDigital, product, prodDenom / Denomgcd;
        
            
            
            
                
            
            