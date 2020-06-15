#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/29 下午6:12
@Author : Catherinexxx
@Site : 
@File : 204. Count Primes.py
@Software: PyCharm
"""
"""
统计所有小于非负整数 n 的质数的数量。
"""
# 约数只有1和它本身的叫质数 2 3 5
# 厄拉多塞筛法
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrimes = [1] * n
        res = 0
        for i in range(2, n):
            if isPrimes[i] == 1: res += 1
            j = i
            while i * j < n:
                isPrimes[i * j] = 0
                j += 1
        return res

# 上面优化
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        return sum(isPrimes)

