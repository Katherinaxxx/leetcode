#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/20 下午9:51
@Author : Catherinexxx
@Site : 
@File : 滴滴2018岛屿.py
@Software: PyCharm
"""
"""
给定一个m行n列的二维地图, 初始化每个单元都是水.
操作addLand 把单元格(row,col)变成陆地.
岛屿定义为一系列相连的被水单元包围的陆地单元, 横向或纵向相邻的陆地称为相连(斜对角不算).
在一系列addLand的操作过程中, 给出每次addLand操作后岛屿的个数.
二维地图的每条边界外侧假定都是水.
"""
import copy


class Solution:
    def numIslands(self, grid):
        res = 0
        for i in range(len(grid[0])):
            for j in range(len(grid[0][0])):
                if grid[i][j] == '1':
                    res += 1
                    self.merge(grid, i, j)
        return res

    def merge(self, grid, i, j):
        if i < 0 or i >= len(grid[0]) or j < 0 or j >= len(grid[0][0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.merge(grid, i+1, j)
        self.merge(grid, i-1, j)
        self.merge(grid, i, j+1)
        self.merge(grid, i, j-1)


m, n, k = [int(input()) for _ in range(3)]
land, grid = [["0" for i in range(n)] for j in range(m)], []
solution = Solution()
res = [0]
for i in range(k):
    row, col = map(int, input().split())
    if row < m and col < n:
        land[row][col] = "1"
        grid = copy.deepcopy(land)
        res.append(str(solution.numIslands(grid)))
    else:
        res.append(res[-1])
print(" ".join(res[1:]))