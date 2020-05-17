#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/17 下午4:09
@Author : Catherinexxx
@Site : 
@File : 79. Word Search.py
@Software: PyCharm
"""
"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# dfs + 回溯（因为单词不能重复使用）
# O((4mn)^2)=O((mn)^2)time O(mn)space
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k, visited):
            if k == len(word):
                return True

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for (dx, dy) in directions:
                if 0 <= i + dx <= m - 1 and 0 <= j + dy <= n - 1 and board[i + dx][j + dy] == word[k] and (
                i + dx, j + dy) not in visited:
                    visited.append((i + dx, j + dy))
                    if dfs(i + dx, j + dy, k + 1, visited):
                        return True
                    visited.remove((i + dx, j + dy))  # 继续找其他方向 需要回溯
            return False

        # 从每个位置开始查找
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 1, [(i, j)]):
                    return True
        return False