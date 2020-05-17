#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/11 下午7:14
@Author : Catherinexxx
@Site : 
@File : 50. Pow(x, n).py
@Software: PyCharm
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2:       # 偶数
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


# 位运算
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 1
        res = 1
        if n < 0: x, n = 1 / x, -n      # 负的也转化成正的
        while n:
            if n & 1: res *= x          # 若n为奇数
            x *= x
            n >>= 1                     # n=n/2
        return res