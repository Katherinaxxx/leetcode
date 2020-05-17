#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/5 下午5:11
@Author : Catherinexxx
@Site : 
@File : 98. Validate Binary Search Tree.py
@Software: PyCharm
"""
'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归 更新最大最小往下判断
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBST(root, min_val, max_val):
            if root == None:
                return True
            # print(root.val)
            if root.val >= max_val or root.val <= min_val:
                return False
            return isBST(root.left, min_val, root.val) and isBST(root.right, root.val, max_val)
        return True if not root else isBST(root.left, float("-inf"), root.val) and isBST(root.right, root.val, float("inf"))
        # []特例