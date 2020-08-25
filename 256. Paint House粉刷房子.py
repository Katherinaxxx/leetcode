#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/19 下午11:16
@Author : Catherinexxx
@Site : 
@File : 256. Paint House粉刷房子.py
@Software: PyCharm
"""


# dp O(mn)
# dp[i][j] 刷第i个房子用第j种颜色的最少花费
# min(dp[i])

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        dp = [[float("inf")] * 3 for _ in range(len(costs))]
        for i in range(3):
            dp[0][i] = costs[0][i]
        for i in range(1, len(costs)):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
        return min(dp[-1])
