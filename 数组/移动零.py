'''
Author: philosophylato
Date: 2022-10-01 16:36:52
LastEditors: philosophylato
LastEditTime: 2022-10-01 21:20:45
Description: your project
version: 1.0
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/all-about-array/x9rh8e/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
def moveZeros(nums):
    n=len(nums)
    i-=1
    j=0
    while j<=n-1:
        if nums[j]!=0:
            i+=1
            nums[i]=nums[j]
        j+=1
    for k in range(i+1,n):
        nums[k]=0
        