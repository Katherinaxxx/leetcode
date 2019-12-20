#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/5 上午11:14
@Author : Catherinexxx
@Site : 
@File : 429. N-ary Tree Level Order Traversal.py
@Software: PyCharm
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# BFD
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        # queue为要找的 out为结果
        queue = [root]
        out = []
        # 当有待查找的
        while queue:
            # child为这一轮结果
            child = []
            # node存这一轮子节点 作为下一轮的queue
            node = []
            for item in queue:
                child.append(item.val)
                if item.children: node += item.children
            # 一轮查找完 赋值给out 更新下一轮queue
            out.append(child)
            queue = node  # 重要!  赋值给新 收集到的 子节点数据
        return out