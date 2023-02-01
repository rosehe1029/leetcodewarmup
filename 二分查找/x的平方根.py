'''
Author: philosophylato
Date: 2022-12-04 20:45:05
LastEditors: philosophylato
LastEditTime: 2022-12-04 20:47:10
Description: your project
version: 1.0
'''
def mysqrt(x):
    low=1
    high=x
    while (low+1 <high):
        mid=low+(high-low)//2
        if (mid*mid <=x):
            low=mid
        else:
            high=mid
    if (high*high <=x):
        return high
    else :
        return low

        
