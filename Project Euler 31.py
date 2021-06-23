# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:03:35 2020

"""

# We don't need to worry about the 1ps because we can take any sum less than 2
# and add 1ps to make up the difference. Also don't worry about £2 as that 
# will only appear once.


def prob31():
    count = 1;
    for j in list(range(101)):
        if 2*j >200:
            break
        for k in list(range(41)):
            if 2*j + 5*k>200:
                break
            for l in list(range(21)):
                if 2*j + 5*k + 10*l >200:
                    break
                for m in list(range(11)):
                    if 2*j + 5*k + 10*l + 20*m >200:
                        break
                    for n in list(range(5)):
                        if 2*j + 5*k + 10*l + 20*m + 50*n > 200:
                            break
                        for o in list(range(3)):
                            if 2*j + 5*k + 10*l + 20*m + 50*n + 100*o > 200:
                                break
                            count += 1;
                            print(j,k,l,m,n,o)
    print(count);
            