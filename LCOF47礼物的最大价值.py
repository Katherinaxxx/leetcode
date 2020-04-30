#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/2/19 下午4:08
@Author : Catherinexxx
@Site : 
@File : LCOF47礼物的最大价值.py
@Software: PyCharm
"""

# DP
# dp[i][j] -- [i,j]最大获得的礼物 需要加一行一列辅助
# dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1] (dp多一行一列)
#
#

class Solution:
    def maxValue(self, grid):
        dp = [[0] * (len(grid[0])+1) for _ in range(len(grid)+1)]
        for i in range(1, len(grid)+1):
            for j in range(1, len(grid[0])+1):
               dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[-1][-1]

print(Solution().maxValue([[1,2,5],[3,2,1]]))