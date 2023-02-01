'''
Author: philosophylato
Date: 2022-12-04 20:16:34
LastEditors: philosophylato
LastEditTime: 2022-12-04 20:23:34
Description: your project
version: 1.0
'''
def search(nums,target):
    l,r=0,len(nums)
    while l+1<r:
        m=(l+r)//2
        if nums[m]<=target:
            l=m
        else:
            r=m
    if nums[l]==target:
        return 1
    else :
        return -1
