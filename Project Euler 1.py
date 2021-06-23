# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
def  divisibleByThree(x):
    if x%3 == 0:
        return True;
    return False;

divisibleByThree(3)

def  divisibleByFive(x):
    if x%5 == 0:
        return True;
    return False;

def multiplyList(myList) :     
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result  
      
def finalFunction(x):
    a = [];
    for number in list(range(1, x)):
        if (divisibleByThree(number) or divisibleByFive(number)):
            a.append(x)
    return multiplyList(a)

print(finalFunction(1000))

print(finalFunction(78))        
            
    


    