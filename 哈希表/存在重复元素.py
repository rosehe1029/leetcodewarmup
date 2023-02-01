'''
Author: philosophylato
Date: 2022-10-27 17:01:25
LastEditors: philosophylato
LastEditTime: 2022-10-27 17:10:29
Description: your project
version: 1.0
'''
def containsDuplicate(nums):
    if len(nums) <=1:
        return False
    
    hashset=set()
    for i in nums:
        if i in hashset:
            return True
        else:
            hashset.add(i)
    return False


