'''
Author: Catherine Xiong
Date: 2022-12-28 18:40:31
LastEditTime: 2022-12-29 20:24:07
LastEditors: Catherine Xiong
Description: 
'''
#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
# DP
# dp[i][j]表示[i,j]为右下角的 最大边长

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        res = 0
        dp = [[0] * (col+1) for i in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j] ** 2)
        return res

# @lc code=end

