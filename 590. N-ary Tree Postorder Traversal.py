#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/5 上午10:30
@Author : Catherinexxx
@Site : 
@File : 590. N-ary Tree Postorder Traversal.py
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
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def recursion(node):
            if not node:
                return
            for i in node.children:
                recursion(i)
            res.append(node.val)

        recursion(root)

        return res