#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/19 下午10:16
@Author : Catherinexxx
@Site : 
@File : 625. Minimum Factorization最小因式分解.py
@Software: PyCharm
"""
class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a < 10:return a
        factor = []
        for i in range(9, 1, -1):
            while a % i == 0:
                factor.append(str(i))
                a //= i
        if a != 1:return 0
        res = int("".join(factor[::-1]))
        return res if res < 2 ** 31 else 0