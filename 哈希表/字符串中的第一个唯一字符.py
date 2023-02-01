'''
Author: philosophylato
Date: 2022-11-02 13:41:07
LastEditors: philosophylato
LastEditTime: 2022-11-02 13:47:41
Description: your projectir
version: 1.0
'''
from collections import Counter
def firstUniqChar(s:str):
    counter=dict(Counter([c for c in s]))
    counter={k:v for k,v in counter.items() if v==1}
    if not counter:
        return -1
    else:
        p=list(counter.keys())[0]
        return s.index(p)