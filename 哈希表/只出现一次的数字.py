'''
Author: philosophylato
Date: 2022-11-01 12:00:51
LastEditors: philosophylato
LastEditTime: 2022-11-01 12:02:06
Description: your project
version: 1.0
'''
def singleNumber(nums):
    hashset=set()
    for num in nums:
        if num in hashset:
            hashset.remove(num)
        else:
            hashset.add(num)
    return hashset.pop()

    