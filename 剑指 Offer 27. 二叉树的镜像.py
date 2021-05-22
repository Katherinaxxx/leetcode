#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/4/21 8:37 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 剑指 Offer 27. 二叉树的镜像.py
@Description: 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归 O(n)
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

# 迭代
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node.left, node.right = node.right, node.left
        return root

