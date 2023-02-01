'''
Author: philosophylato
Date: 2022-11-02 14:11:57
LastEditors: philosophylato
LastEditTime: 2022-11-02 14:14:03
Description: your project
version: 1.0
'''
def containsNearbyDuplicate(nums,k):
    data={}
    for index,value in enumerate(nums):
        if index in data and index-data[value] <=k:
            return True
        data[value]=index
    return False
    
