#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/23 下午3:03
@Author : Catherinexxx
@Site : 
@File : 85. Maximal Rectangle.py
@Software: PyCharm
"""
"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
"""
# 类似84.largest-rectangle-in-histogram 找到高度 之后用栈更新面积
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0    # 判特

        row = len(matrix)
        col = len(matrix[0])
        height = [0] * (col + 2)
        res = 0
        # 开始找height（每一行的） 找到后更新面积（每一行更新一次）
        for i in range(row):
            stack = []
            for j in range(col + 2):
                if 1<=j<=col:
                    # 若当前位置上一个位置==1
                    if matrix[i][j-1] == "1":
                        height[j] += 1
                    else:
                        height[j] = 0
                # 之后跟84一样
                while stack and height[stack[-1]] > height[j]:
                    cur = stack.pop()
                    res = max(res, (j - stack[-1] - 1)* height[cur])
                stack.append(j)
        return res