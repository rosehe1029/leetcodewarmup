'''
Author: philosophylato
Date: 2022-10-03 14:53:41
LastEditors: philosophylato
LastEditTime: 2022-10-03 14:55:16
Description: your project
version: 1.0
'''
'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/array-and-string/yf47s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''
def pivotIndex(nums):
    all=sum(nums)
    left=0
    for i in range(len(nums)):
        if left *2 +nums[i]==all:
            return i
        else :
            left+=nums[i]
    return -1