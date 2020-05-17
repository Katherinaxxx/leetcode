#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/1 下午1:37
@Author : Catherinexxx
@Site : 
@File : 114. Flatten Binary Tree to Linked List.py
@Software: PyCharm
"""
"""
给定一个二叉树，原地将它展开为链表。
"""
# 迭代
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            # 左边有
            if cur.left:
                p = cur.left
                while p.right: p = p.right  # 找到左边最右的节点
                p.right = cur.right         # 把右边移到左边最右的右边
                cur.right = cur.left
                cur.left = None
            # 左边没有则直接看右边
            cur = cur.right