# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:05:50 2019

"""
def Problem19(upperBound):
    A = [31,28,31,30,31,30,31,31,30,31,30,31];
    day = sum(A);
    Sundays = 0;
    for year in list(range(1901, upperBound +1)):
        for month in A:
            day += 1;
            if day %7 == 0:
                 Sundays +=1;
            day += month - 1;
            if (year % 100 != 0 and year % 4 == 0 and month == 28) or (year % 100 == 0 and year % 400 == 0 and month == 28):
                day += 1;
#            for x in list(range(1, month+1)):
#                day += 1;
    return f"The number of Sundays that fall on the first of the month between 1901 and 2000 is {Sundays}";
                
                