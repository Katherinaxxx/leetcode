#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/17 上午10:57
@Author : Catherinexxx
@Site : 
@File : 70.climbing-stairs.py
@Software: PyCharm
"""

"""
1:1
2:2
3:f(1)+f(2)
4:f(2)+f(3)
.... Fabonacci
"""
# 动态规划 数组
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3

# 优化 更DP
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i - 1] + f[i - 2])
        return f[n - 1]

# 递归超时
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         res = 0
#         def recursion(cur):
#             nonlocal res
#             if cur == 0:
#                 res += 1
#                 return
#             if cur < 0:
#                 return

#             recursion(cur-1)
#             recursion(cur-2)
#         recursion(n)
#         return res