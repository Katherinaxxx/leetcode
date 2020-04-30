#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/28 下午2:30
@Author : Catherinexxx
@Site : 
@File : 538. Convert BST to Greater Tree.py
@Software: PyCharm
"""
'''
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 右中左 储存节点
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = [(root, 1)]
        s = 0
        while stack:
            node, flag = stack.pop()

            # 如果为空则看下一个
            if node is None:
                continue

            # 如果没有可加的 则求和
            if flag == 0:
                s += node.val
                node.val = s

            # 否则继续加如stack
            else:
                stack.append((node.left, 1))
                stack.append((node, 0))
                stack.append((node.right, 1))

        return root
