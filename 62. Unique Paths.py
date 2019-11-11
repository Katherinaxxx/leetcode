#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/11 下午1:18
@Author : Catherinexxx
@Site : 
@File : 62. Unique Paths.py
@Software: PyCharm
"""

# 自己第一次写比较复杂
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#
#         down = [1] * (n - 1)
#         cur = [0] * (n - 1) + [1]
#         for row in range(m - 1):
#             for col in range(n - 2, -1, -1):
#                 cur[col] = down[col] + cur[col + 1]
#                 print(cur)
#             if row == m-2:
#                 return cur[0]
#
#             down = cur
#             cur = [0] * (n - 1) + [1]

# DP二维
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# DP一维
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

print(Solution().uniquePaths(3,2))