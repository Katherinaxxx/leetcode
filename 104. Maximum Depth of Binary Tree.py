#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/6 上午10:32
@Author : Catherinexxx
@Site : 
@File : 104. Maximum Depth of Binary Tree.py
@Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0

        def recursion(node, depth):
            nonlocal max_depth
            if not node:
                max_depth = max(max_depth, depth)
                return
            recursion(node.left, depth + 1)
            recursion(node.right, depth + 1)

        recursion(root, 0)
        return max_depth


# 只是短 非常慢
class Solution:

    def maxDepth(self, root):
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0