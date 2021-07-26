#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/7/26 10:44 PM
@Author : Catherinexxx
@File : 剑指 Offer 32 - II. 从上到下打印二叉树 II.py
@Description: 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(n) time O(n) space
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur_res = []
            for _ in range(len(queue)):
                cur = queue.popleft()   # 双端队列O(1) list O(n)
                cur_res.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            res.append(cur_res)
        return res


