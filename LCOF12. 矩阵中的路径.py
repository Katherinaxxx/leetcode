#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/10 10:33 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : LCOF12. 矩阵中的路径.py
@Description: 
"""
"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# O(n
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isValid(i, j):
            return 0<=i<m and 0<=j<n

        def DFS(i, j, seen):
            if len(seen) >= len(word):
                return True
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i+dx, j+dy
                if isValid(x, y) and word[len(seen)] == board[x][y] and (x, y) not in seen:
                    seen.add((x, y))
                    if DFS(x, y, seen):
                        return True
                    # 回溯
                    seen.discard((x, y))
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                # 起点 且 有后续的
                if board[i][j] == word[0] and DFS(i, j, {(i, j)}):
                    return True
        return False

# 非递归
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 预处理
        w_l = len(word)
        if w_l < 1:
            return True
        rows = len(board)
        cols = len(board[0])
        # 标记数组
        board_vis = [[0] * cols for i in range(rows)]
        # 方向数组
        dir_list = [[-1, 0], [0, 1], [1, 0],[0, -1]]
        # 非递归DFS要用栈维护哦，先把所有头节点放进来，每个节点包括3个值（i,j,l）,i和j是它的坐标，l是它在word中的下标
        word_stack = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    word_stack.append((i, j, 0))
        # 正式开始DFS咯
        while len(word_stack) > 0:
            # 获取头节点信息，先不要弹出
            top = word_stack[-1]
            tx = top[0]
            ty = top[1]
            tl = top[2]
            # 访问这个节点，并开始深度遍历
            board_vis[tx][ty] = 1
            # 出口条件，如果word遍历完，返回True
            if tl == w_l - 1:
                return True
            # flag记录是否能够继续深度遍历
            flag = True
            for di in dir_list:
                next_x = tx + di[0]
                next_y = ty + di[1]
                # 深度遍历的条件
                if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols \
                        and board_vis[next_x][next_y] == 0 and board[next_x][next_y] == word[tl + 1]:
                    # 注意子节点与父节点的关系
                    word_stack.append((next_x, next_y, tl + 1))
                    flag = False
            # 如果不能继续深度遍历，回溯，这个回溯有点复杂：需要一层一层往上回溯，回溯到有多个子节点的地方，类似于树的深度遍历
            if flag:
                while len(word_stack):
                    top = word_stack[-1]
                    if top[2] != tl:
                        break
                    tl -= 1
                    # 弹出，并标记取消
                    word_stack.pop()
                    board_vis[top[0]][top[1]] = 0
        return False
