#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/13 上午10:19
@Author : Catherinexxx
@Site : 
@File : 120. Triangle.py
@Software: PyCharm
"""
# 1、暴力 递归每种路径 求最小 O(2^n)
# 2、DP
# a.重复性（分治）problem(i,j) = min(sub(i+1,j), sub(i+1,j+1)) + a[i,j]
# b.定义状态数组 f[i,j]
# c.DP方程 f[i,j] = min(f[i+1,j], f[i+1,j+1]) + a[i,j]
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]

# bottom-up, O(n) space  一维状态数组
class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]