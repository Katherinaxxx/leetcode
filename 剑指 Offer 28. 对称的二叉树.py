#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/4/21 8:53 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 剑指 Offer 28. 对称的二叉树.py
@Description: 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)