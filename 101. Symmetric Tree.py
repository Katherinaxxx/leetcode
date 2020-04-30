#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/29 下午5:15
@Author : Catherinexxx
@Site : 
@File : 101. Symmetric Tree.py
@Software: PyCharm
"""
'''
给定一个二叉树，检查它是否是镜像对称的
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recursion(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return recursion(left.left, right.right) and recursion(left.right, right.left)
        return recursion(root.left, root.right) if root else True

