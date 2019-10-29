#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/28 下午3:50
@Author : Catherinexxx
@Site : 
@File : 102. Binary Tree Level Order Traversal.py
@Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        def DFS(node, level):
            if len(res) == level:
                res.append([])

            res[level].append(node.val)

            if node.left:
                DFS(node.left, level + 1)
            if node.right:
                DFS(node.right, level + 1)

        DFS(root, 0)
        return res
# # BFS
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root: return []
#         res = []
#         cur_level = [root]
#         while cur_level:
#             tmp = []
#             next_level = []
#             for node in cur_level:
#                 tmp.append(node.val)
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
#             res.append(tmp)
#             cur_level = next_level
#         return res

