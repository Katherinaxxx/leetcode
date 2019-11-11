#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/6 上午11:05
@Author : Catherinexxx
@Site : 
@File : 111. Minimum Depth of Binary Tree.py
@Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        children = [root.left, root.right]
        # if we're at leaf node
        if not any(children):
            return 1

        min_depth = float('inf')

        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1