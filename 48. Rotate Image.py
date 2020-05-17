#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/6 下午1:36
@Author : Catherinexxx
@Site : 
@File : 48. Rotate Image.py
@Software: PyCharm
"""

'''
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。
'''

# 由内向外 一层一层地转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper(ix, iy, jx, jy):     # 左上和右下的坐标
            length = jx - ix + 1
            if length <= 1:             # 奇数= 偶数<
                return
            for i in range(length-1):
                matrix[ix][iy+i], matrix[ix+i][jy], matrix[jx][jy-i], matrix[jx-i][ix] = matrix[jx-i][ix], matrix[ix][iy+i], matrix[ix+i][jy], matrix[jx][jy-i]
            helper(ix+1, iy+1, jx-1, jy-1)
        helper(0,0,len(matrix)-1,len(matrix)-1)

# 光头哥 先reverse() 再交换对角元素
class Solution:
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]