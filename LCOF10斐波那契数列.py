#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/2/20 下午2:00
@Author : Catherinexxx
@Site : 
@File : LCOF10斐波那契数列.py
@Software: PyCharm
"""

# %1000000007 可以保证值永远在int的范围内
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        f1, f2, f3 = 0, 1, 1
        for i in range(n-1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3%1000000007

# dp
class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        for i in range(2, n+1):
            f.append(f[i - 1] + f[i - 2])
        return f[n]%1000000007

# # lru_cache + 递归
# import functools
# class Solution:
#     @functools.lru_cache
#     def fib(self, n: int) -> int:
#         return n if n < 2 else (self.fib(n-1) + self.fib(n-2))%1000000007
