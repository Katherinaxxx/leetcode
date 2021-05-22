#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/4 6:28 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 1473. 粉刷房子 III.py
@Description: 在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。有的房子去年夏天已经涂过颜色了，所以这些房子不需要被重新涂色。
"""


# dfs 超时 @lru_cache(None)不超时
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(i, t, pre_color):
            if t == -1 or i + t > m:
                return float("inf")
            if i == m:
                # 所有房子遍历完
                return 0
            if houses[i] != 0:
                # 已被涂
                return dfs(i + 1, t if houses[i] == pre_color else t - 1, houses[i])
            else:
                # 未被涂
                return min(dfs(i + 1, t if j + 1 == pre_color else t - 1, j + 1) + cost[i][j] for j in range(n))

        ans = dfs(0, target, -1)
        return ans if ans != float("inf") else -1

















