#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/14 下午2:37
@Author : Catherinexxx
@Site : 
@File : 118. Pascal's Triangle.py
@Software: PyCharm
"""
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""


# 直接算  O(n)*O(n-2)
class Solution:
    def generate(self, numRows: int):
        if numRows <= 2: return [[1]*_ for _ in range(1, numRows+1)]
        res = [[1]*_ for _ in range(1, 2+1)]
        for i in range(2, numRows):
            cur_level = [1]
            for j in range(len(res[-1])-1):
                cur_level.append(res[-1][j]+res[-1][j+1])
            cur_level.append(1)
            res.append(cur_level)
        return res
# python优化 【0】 1 3 3 1 + 1 3 3 1 【0】对应相加
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res


print(Solution().generate(14))