#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/17 10:23 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 993. 二叉树的堂兄弟节点.py
@Description: 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth, x_parent, y_depth, y_parent = None, None, None, None

        # 标准dfs模板, 只是在中间加了一些判断逻辑
        def dfs(root, parent, x, y, depth):
            nonlocal x_depth, x_parent, y_depth, y_parent
            if root is None:
                return

                # 判断 x, y 是否等于当前节点的值, 是的话更新 x 或者 y 的深度和parent
            if root.val == x:
                x_depth = depth
                x_parent = parent
            if root.val == y:
                y_depth = depth
                y_parent = parent

            dfs(root.left, root, x, y, depth + 1)
            dfs(root.right, root, x, y, depth + 1)

        dfs(root, None, x, y, 0)
        # 最后保证 x, y的深度一样, 但是parent节点不一样, 这样才是堂兄弟
        return x_depth == y_depth and x_parent != y_parent







