#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/14 上午11:29
@Author : Catherinexxx
@Site : 
@File : 322. Coin Change.py
@Software: PyCharm
"""


# 1、暴力 递归
# 2、BFS
# 3、DP
# num[n] = sum(num[n-k]) for k in coins + 1
# 自底向下
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else float("inf") for c in coins) + 1
        return dp[-1] if dp[-1] != float("inf") else -1