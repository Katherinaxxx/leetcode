#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/25 上午12:03
@Author : Catherinexxx
@Site : 
@File : 235. Lowest Common Ancestor of a Binary Search Tree二叉搜索树的最近公共祖先.py
@Software: PyCharm
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""

 利用二叉搜索树的特点，如果p、q的值都小于root，说明p q 肯定在root的左子树中；如果p q都大于root，说明肯定在root的右子树中，如果一个在左一个在右 则说明此时的root记为对应的最近公共祖先
 """


# 1 递归 O(n)time O(n)space
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root


# 迭代 O(n)time
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p.val > parent_val and q.val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p.val < parent_val and q.val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node

