'''
Author: philosophylato
Date: 2022-10-01 22:20:48
LastEditors: philosophylato
LastEditTime: 2022-10-01 22:20:53
Description: your project
version: 1.0
'''
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = 0
        j = n - 1

        maxarea = (j - i) * min(height[i], height[j])
        
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            maxarea = max(maxarea, (j - i) * min(height[i], height[j]))
            
        return maxarea