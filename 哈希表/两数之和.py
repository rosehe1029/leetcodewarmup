'''
Author: philosophylato
Date: 2022-10-27 17:19:21
LastEditors: philosophylato
LastEditTime: 2022-10-27 17:27:33
Description: your project 
version: 1.0
'''
def twoSum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        if (target -nums[i]) in hashmap:
            return hashmap[target-nums[i]],i
        hashmap[nums[i]]=i
        
