#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/12 下午6:36
@Author : Catherinexxx
@Site : 
@File : 279. Perfect Squares.py
@Software: PyCharm
"""
"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
你需要让组成和的完全平方数的个数最少。
"""

# 类似于coin change O(n*n^0.5)time O(n)space

class Solution:
    def numSquares(self, n: int) -> int:
        # 自底向上
        # dp[i] 表示为i需要最少的完全平方数
        # dp[i] = min(dp[i], dp[i - j*j]) j为小于i的数
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = i
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i - j*j]+1)
        return dp[-1]