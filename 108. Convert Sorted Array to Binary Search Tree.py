#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/28 下午12:32
@Author : Catherinexxx
@Site : 
@File : 108. Convert Sorted Array to Binary Search Tree.py
@Software: PyCharm
"""
"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二分 递归 O(n)time

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            m = len(nums) // 2
            r = TreeNode(nums[m])
            r.left, r.right = map(self.sortedArrayToBST, [nums[:m], nums[m+1:]])
            return r
