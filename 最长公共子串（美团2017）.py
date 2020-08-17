#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/13 下午10:41
@Author : Catherinexxx
@Site : 
@File : 最长公共子串（美团2017）.py
@Software: PyCharm
"""
class Solution:
    def longestCommon(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res