#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/6/28 10:29 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 剑指 Offer 26. 树的子结构.py
@Description: 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
isSubStructure函数的返回值，若树 B 是树 A 的子结构，则必满足以下三种情况之一：

以 节点 A 为根节点的子树 包含树 B ，对应 recur(A, B)；
树 B 是 树 A 左子树 的子结构，对应 isSubStructure(A.left, B)；
树 B 是 树 A 右子树 的子结构，对应 isSubStructure(A.right, B)；
recur函数的终止条件：

当节点 B 为空：说明树 B 已匹配完成（越过叶子节点），因此返回 true ；
当节点 A 为空：说明已经越过树 A 叶子节点，即匹配失败，返回 false ；
当节点 A 和 B 的值不同：说明匹配失败，返回 false ；
返回值：

判断 A 和 B 的左子节点是否相等，即 recur(A.left, B.left) ；
判断 A 和 B 的右子节点是否相等，即 recur(A.right, B.right)
"""
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
    def dfs(self, a, b):
        if not b:
            return True
        elif not a:
            return False
        elif a.val != b.val:
            return False
        else:
            return self.dfs(a.left, b.left) and self.dfs(a.right, b.right)