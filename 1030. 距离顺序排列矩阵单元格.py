#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/17 9:46 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 1030. 距离顺序排列矩阵单元格.py
@Description: 给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。

另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。

返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-cells-in-distance-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 暴力  O(rclogrc) O(logrc)
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        return sorted(((i, j) for i in range(R) for j in range(C)), key=lambda x:abs(x[0]-r0)+abs(x[1]-c0))

# 桶排序  O(rc) O(rc)
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        maxDist = max(r0, abs(R-r0-1)) + max(c0, abs(C-c0-1))
        bucket = collections.defaultdict(list)
        dis = lambda x,y: abs(x-r0)+abs(y-c0)
        for i in range(R):
            for j in range(C):
                bucket[dis(i, j)].append([i, j])
        res = []
        for i in range(maxDist+1):
            res.extend(bucket[i])

        return res

# bfs 上下左右每走一步距离加一
from collections import deque
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        qu = deque([(r0, c0)])
        seen = set()
        seen.add((r0, c0))
        ans = []
        while qu:
            cur = qu.popleft()
            ans.append(cur)
            for dx, dy in direction:
                new_x = cur[0] + dx
                new_y = cur[1] + dy
                if 0 <= new_x < R and 0 <= new_y < C and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    qu.append((new_x, new_y))
        return ans

# 几何法
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        row, col = r0, c0
        ret = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    if 0 <= row < R and 0 <= col < C:
                        ret.append([row, col])
                    row += dr
                    col += dc
        return ret
