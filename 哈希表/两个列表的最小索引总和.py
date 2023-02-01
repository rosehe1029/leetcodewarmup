'''
Author: philosophylato
Date: 2022-11-01 22:28:55
LastEditors: philosophylato
LastEditTime: 2022-11-01 22:40:23
Description: your project
version: 1.0
'''
from email.policy import default


def findRestaurant(list1,list2):
    a={v:i for i,v in enumerate(list1)}
    b=defaultdict(list)
    mi=2001
    for i,v in enumerate(list2):
        if v in a:
            mi=min(mi,a[v]+i)
            b[a[v]+i].append(v)
    return b[mi]










