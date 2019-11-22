#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/12 上午11:06
@Author : Catherinexxx
@Site : 
@File : 63. Unique Paths II.py
@Software: PyCharm
"""
# 给左、上加辅助边
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [1] + [0]*m
        for i in range(0, n):
            for j in range(0, m):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j]+dp[j-1]
        return dp[-2]