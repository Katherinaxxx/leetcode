#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/2/20 下午2:14
@Author : Catherinexxx
@Site : 
@File : 509.LCOF青蛙跳台阶问题.py
@Software: PyCharm
"""
# fn = fn-1 + fn-2
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0 :return 1
        if n <= 2: return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n+1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3%1000000007