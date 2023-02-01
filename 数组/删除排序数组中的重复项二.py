'''
Author: philosophylato
Date: 2022-10-01 21:30:35
LastEditors: philosophylato
LastEditTime: 2022-10-01 21:34:19
Description: your project
version: 1.0
'''
from tkinter import N


def removeDuplicates(nums):
    n=len(nums)
    if (n<=2):
        return n 
    i=1
    k=i-1
    j=i+1
    while j<=n-1:
        if (nums[j]!=nums[i]) or (nums[j]==nums[i] and nums[j]!=nums[k]):
            k=i
            nums[i+1]=nums[j]
            i+=1
        j+=1
    return i+1
    


