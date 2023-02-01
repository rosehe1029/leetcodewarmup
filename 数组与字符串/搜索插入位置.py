'''
Author: philosophylato
Date: 2022-10-03 15:06:28
LastEditors: philosophylato
LastEditTime: 2022-10-10 10:30:02
Description: your project
version: 1.0
'''
import re
from turtle import right


def searchInsert(nums,target):
    if len(nums)<1:return 0
    left=0
    right=len(nums)-1
    while (left<=right):
        mid=left+(right-left)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] >target:
            right=mid-1
        else:
            left=mid+1
    return right +1


