#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/28 下午1:08
@Author : Catherinexxx
@Site : 
@File : 226. Invert Binary Tree.py
@Software: PyCharm
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 左右交换
# 递归
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

# 栈模拟递归
class Solution:
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node.left)
        return root
