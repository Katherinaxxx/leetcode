'''
Author: Catherine Xiong
Date: 2021-12-07 18:28:45
LastEditTime: 2021-12-07 19:07:10
LastEditors: Catherine Xiong
Description: 给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。

两个网格块属于同一 连通分量 需满足下述全部条件：

两个网格块颜色相同
在上、下、左、右任意一个方向上相邻
连通分量的边界 是指连通分量中满足下述条件之一的所有网格块：

在上、下、左、右四个方向上与不属于同一连通分量的网格块相邻
在网格的边界上（第一行/列或最后一行/列）
请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coloring-a-border
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。    
'''
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        explored = set()

        def dfs(r, c):
            # 边界
            if r < 0 or c < 0 or r == m or c == n:
                return True
            # 走过
            if (r,c) in explored:
                return False
            # 不等
            if grid[r][c] != grid[row][col]:
                return True
            explored.add((r,c))
            ans = False
            # 判断当前点是否满足要求
            for dx,dy in (0,1),(1,0),(0,-1),(-1,0):
                if dfs(r+dx,c+dy):
                    ans = True
            if ans:
                grid[r][c] = color
            return False
        
        dfs(row, col)
        return grid

