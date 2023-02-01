'''
Author: philosophylato
Date: 2022-12-04 20:33:46
LastEditors: philosophylato
LastEditTime: 2022-12-04 20:36:42
Description: your project
version: 1.0
'''
def findPeakElement(nums):
    lo,hi=0,len(nums)-1
    while lo <hi:
        mid=(lo+hi)//2
        if nums[mid]<nums[mid+1]:lo=mid+1
        else:hi=mid
    return lo
    
