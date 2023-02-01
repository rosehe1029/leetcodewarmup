'''
Author: philosophylato
Date: 2022-10-01 21:21:27
LastEditors: philosophylato
LastEditTime: 2022-10-01 21:24:35
Description: your project
version: 1.0

'''
def removeElement(nums,val):
    n=len(nums)
    i=-1
    j=0
    while j<=n-1:
        if nums[j] != val:
            i+=1
            nums[i]=nums[j]
        j+=1
    return i+1
    

