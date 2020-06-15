#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/13 下午4:34
@Author : Catherinexxx
@Site : 
@File : 103. Binary Tree Zigzag Level Order Traversal.py
@Software: PyCharm
"""
"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS O(n) 用深度来区分从左还是从右
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        cur_level = [root]
        depth = 0
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if depth % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            depth += 1
            cur_level = next_level
        return res


# DFS
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(root, depth):
            if not root: return
            if len(res) == depth:
                res.append([])
            if depth % 2 == 0:
                res[depth].append(root.val)
            else:
                res[depth].insert(0, root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return res