#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/1 下午12:18
@Author : Catherinexxx
@Site : 
@File : 124. Binary Tree Maximum Path Sum.py
@Software: PyCharm
"""
"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归 O(n)time O(logn)space
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
            self.res = float("-inf")
            def helper(root):
                if not root: return 0
                # 左边最大值
                left = helper(root.left)
                # 右边最大值
                right = helper(root.right)
                # 和全局变量比较
                self.res = max(left + right + root.val, self.res)
                # >0 说明都能使路径变大
                return max(0, max(left,  right) + root.val)
            helper(root)
            return self.res