#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/24 下午10:41
@Author : Catherinexxx
@Site : 
@File : 54. 螺旋矩阵Spiral Matrix.py
@Software: PyCharm
"""

# 遍历 + 取余数调整遍历方向 time O(n)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        x, y = 0, 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        direction = 0
        visited = set()
        for i in range(len(matrix)*len(matrix[0])):
            visited.add((x,y))
            res.append(matrix[x][y])
            # 如果下一个数不在visited中 且下一个数的索引没有超出范围 则方向不变 继续走
            if (x+dx[direction],y+dy[direction]) not in visited and 0<=x+dx[direction]<len(matrix) and 0<=y+dy[direction]<len(matrix[0]):
                pass
            else:
                direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]
        return res


