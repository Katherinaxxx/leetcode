#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/12/4 上午10:31
@Author : Catherinexxx
@Site : 
@File : 72. Edit Distance.py
@Software: PyCharm
"""
# DP
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = j
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = i
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        #print(dp)
        return dp[-1][-1]