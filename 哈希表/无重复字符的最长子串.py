'''
Author: philosophylato
Date: 2022-11-02 15:13:12
LastEditors: philosophylato
LastEditTime: 2022-11-02 15:14:22
Description: your projectenfr
version: 1.0
'''
def LengthOfLongestSubstring(s):
    dct,res,prev={},0,-1
    for i,v in enumerate(s):
        if v in dct and prev <dct[v]:
            n=i-dct[v]
            prev=dct[v]
        else :
            n=i-prev
        res=n if n>res else res
        dct[v]=i
    return res
    