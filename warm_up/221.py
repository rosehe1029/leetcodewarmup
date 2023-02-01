'''
Author: philosophylato
Date: 2022-09-11 17:23:10
LastEditors: philosophylato
LastEditTime: 2022-09-11 17:49:38
Description: your project
version: 1.0
'''
'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maximalSquare(self, matrix) -> int:
        res = 0
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1" :
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 
                    res = max(res, dp[i][j])
        return res ** 2

matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]


