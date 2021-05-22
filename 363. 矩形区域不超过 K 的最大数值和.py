#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/4/22 1:37 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 363. 矩形区域不超过 K 的最大数值和.py
@Description: 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
"""
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            # 以left为左边界，每行的总和
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                # 在left，right为边界下的矩阵，求不超过K的最大数值和
                arr = [0]
                cur = 0
                for tmp in _sum:
                    cur += tmp
                    # 二分法
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)
        return res

