'''
Author: philosophylato
Date: 2022-10-01 21:35:43
LastEditors: philosophylato
LastEditTime: 2022-10-01 21:41:34
Description: your project
version: 1.0
'''
from tkinter import N


def sortColors(nums):
    n=len(nums)
    lt=-1
    gt=n 
    i=0
    while i<gt:
        if nums[i]==0:
            lt+=1
            nums[lt],nums[i]=nums[i],nums[lt]
        elif nums[i]==2:
            gt-=1
            nums[gt],nums[i]=nums[i],nums[gt]
        else:
            i+=1
            
