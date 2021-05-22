#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/21 5:39 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 1035. 不相交的线.py
@Description: 在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：

 nums1[i] == nums2[j]
且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

以这种方法绘制线条，并返回可以绘制的最大连线数。
"""


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        # 二维数组创建, 注意各个维度的创建顺序
        # dp 数组的处理上, 两个维度都各增加一位
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                # 因为 i, j 是相对dp数组来说的, 多加了一位, 因此读取 nums的时候要 -1
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        return dp[m][n]
