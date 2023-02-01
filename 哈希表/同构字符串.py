'''
Author: philosophylato
Date: 2022-10-27 17:36:22
LastEditors: philosophylato
LastEditTime: 2022-10-27 17:42:47
Description: your project
version: 1.0
'''

def isIsomorphic(s:str,t:str):
    seen1={}
    seen2={}

    for idx,_ in enumerate(s):
        if s[idx] not in seen1:
            seen1[s[idx]]=idx
        if t[idx] not in seen2:
            seen2[t[idx]]=idx
        
        if seen1[s[idx]]!=seen2[t[idx]]:return False
    
    return True

    