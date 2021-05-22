#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/10 11:07 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 872. 叶子相似的树.py
@Description: 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/leaf-similar-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1, leaves2 = [], []

        def preorder(root, leaf):
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            if root.left:
                preorder(root.left, leaf)
            if root.right:
                preorder(root.right, leaf)

        preorder(root1, leaves1)
        preorder(root2, leaves2)
        return leaves1 == leaves2

