#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/28 下午12:31
@Author : Catherinexxx
@Site : 
@File : 461. Hamming Distance.py
@Software: PyCharm
"""

'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。
'''

# 老实算
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while True:  # 一直循环，商为0时利用break退出循环
            s1, s2 = x // 2, y // 2  # 商
            y1, y2 = x % 2,  y % 2  # 余数
            if y1 != y2:
                res += 1
            if s1 == 0 and s2==0 and y1==0 and y2==0:
                break  # 余数和商均为0时结束循环
            x, y = s1, s2
        return res

# 异或xor
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
