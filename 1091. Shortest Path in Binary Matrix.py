#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/22 下午2:48
@Author : Catherinexxx
@Site : 
@File : 1091. Shortest Path in Binary Matrix.py
@Software: PyCharm
"""


# BFS
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        queue, n = [[0, 0, 2]], len(grid)
        if n <= 2: return n

        while queue:
            next_queue = []
            # i, j, dist = queue.pop()
            for i, j, dist in queue:

                for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [-1, -1], [1, 1], [-1, 1]]:
                    cur_x, cur_y = i + x, j + y
                    if cur_x == cur_y == n - 1:
                        return dist
                    if 0 <= cur_x < n and 0 <= cur_y < n and grid[cur_x][cur_y] == 0:
                        grid[cur_x][cur_y] = 1

                        next_queue.append([cur_x, cur_y, dist + 1])
            queue = next_queue

        return -1

# # DP
# a s[i][j] = min(s[八连通])+1 :return s[-1][-1]
# b 0 0....,0....,......
# # A*