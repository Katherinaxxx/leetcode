#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/7 上午11:59
@Author : Catherinexxx
@Site : 
@File : 96. Unique Binary Search Trees.py
@Software: PyCharm
"""
"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
"""

# 卡特兰数问题 DP  O(n^2)time O(n)space
# 设G(n)为1-n形成的二叉搜索树的种数
# f(i)表示以i为根节点的二叉搜索树的种数
# G(n)=f(1)+f(2)+...+f(n)
# f(i)=G(i-1)G(n-i-1)
# 综合， G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)=sigma{i=0,i=n-1}G(i)*G(n-i-1)
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[-1]
