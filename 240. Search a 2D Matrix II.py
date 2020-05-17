#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/17 下午6:33
@Author : Catherinexxx
@Site : 
@File : 240. Search a 2D Matrix II.py
@Software: PyCharm
"""
"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 从左下角出发 若cur<target 当前行排除 i-1上移 若cur>target 当前列排除 j+1
# O(mn)time O(1)space
# 同理可以从左上角出发
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i, j = len(matrix)-1, 0
        while len(matrix)>i>=0 and 0<=j<len(matrix[0]):
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i -= 1
            if matrix[i][j] < target:
                j += 1
        return False