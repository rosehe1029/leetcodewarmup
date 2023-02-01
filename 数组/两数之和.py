'''
Author: philosophylato
Date: 2022-10-01 22:07:16
LastEditors: philosophylato
LastEditTime: 2022-10-01 22:10:36
Description: your project
version: 1.0
'''
def twoSum(numbers,target):
    n=len(numbers)
    if (n<2):
        return []
    i=0
    j=n-1
    while i<j:
        if numbers[j]+numbers[i]==target:
            return [i+1,j+1]
        elif numbers[i] +numbers[j]<target:
            i+=1
        else :
            j-=1
    return []