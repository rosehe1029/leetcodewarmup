'''
Author: philosophylato
Date: 2022-10-01 21:26:03
LastEditors: philosophylato
LastEditTime: 2022-10-01 21:28:32
Description: your project
version: 1.0
'''
from tkinter import N


def removeDuplicates(nums):
    n=len(nums)
    if n==0 or n==1:
        return n 
    i=0
    j=i+1
    while j<=n-1:
        if nums[j]!=nums[i]:
            if i+j !=j:
                nums[i+1]=nums[j]
            i+=1
        j+=1
    return i+1
    

