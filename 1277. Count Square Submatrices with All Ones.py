#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/26 下午1:38
@Author : Catherinexxx
@Site : 
@File : 1277. Count Square Submatrices with All Ones.py
@Software: PyCharm
"""
"""
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
"""

# 和221. Maximal Square 思路相同 只不过结果计数不一样
class Solution:
    def countSquares(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        res = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res += dp[i][j]
        return res