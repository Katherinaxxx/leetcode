#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/3 下午11:11
@Author : Catherinexxx
@Site : 
@File : 110. Balanced Binary Tree平衡二叉树.py
@Software: PyCharm
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root: return True
            left = check(root.left)
            right = check(root.right)
            if not left or not right or abs(left-right)>1:
                return False
            return 1 + max(left, right)
        return check(root) != False