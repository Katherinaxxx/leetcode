#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/7/28 9:07 PM
@Author : Catherinexxx
@File : 剑指 Offer 55 - I. 二叉树的深度.py
@Description: 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归dfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.maxDepth = 0
        if not root: return self.maxDepth

        def dfs(root, depth):
            if root.left:
                dfs(root.left, depth + 1)
            if root.right:
                dfs(root.right, depth + 1)
            self.maxDepth = max(self.maxDepth, depth)

        dfs(root, 1)
        return self.maxDepth


# 迭代
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = collections.deque()
        queue.append(root)
        maxDepth = 0
        while queue:
            l = len(queue)
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            maxDepth += 1
        return maxDepth


