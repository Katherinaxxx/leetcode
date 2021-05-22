#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/4/19 9:03 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 剑指 Offer 04. 二维数组中的查找.py
@Description: 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 可以从左下或者右上开始查找； ps左上和右下不可以（路径不唯一）
# 时间复杂度O(logn) 空间复杂度O(1)
# 以右上为例
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        i, j = 0, len(matrix[0]) - 1
        while i <= len(matrix)-1 and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] == target:
                return True
        return False
