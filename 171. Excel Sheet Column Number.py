#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/10 下午12:48
@Author : Catherinexxx
@Site : 
@File : 171. Excel Sheet Column Number.py
@Software: PyCharm
"""
"""
给定一个Excel表格中的列名称，返回其相应的列序号。

"""

# 从后往前 O(n) 字典
class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        res = 0
        for i in range(n-1, -1, -1):
            res += dict[s[i]]*26**(n-1-i)
        return res
# unicode构建字典
class Solution:
    def titleToNumber(self, s: str) -> int:
        alpha = {}
        # 大写字母对应的顺序字典,A对应的Unicode码为65,Z为90
        for i in range(65, 91):
            alpha[chr(i)] = i-64
        # print(alpha)
        res = 0
        # 列号从右往左每个字母算出数值
        for i in range(len(s)-1, -1, -1):
            res += alpha[s[i]]*pow(26, len(s)-1-i)
        return res

# 26转10进制
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        bit = 1
        for a in s[::-1]:
            res += (ord(a) - 64) * bit
            bit *= 26
        return res