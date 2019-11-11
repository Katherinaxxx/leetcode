#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/5 上午11:13
@Author : Catherinexxx
@Site : 
@File : 589. N-ary Tree Preorder Traversal.py
@Software: PyCharm
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def recursion(node):
            if not node:
                return
            res.append(node.val)
            for i in node.children:
                recursion(i)
        recursion(root)
        return res