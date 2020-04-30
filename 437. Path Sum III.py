#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/29 下午2:11
@Author : Catherinexxx
@Site : 
@File : 437. Path Sum III.py
@Software: PyCharm
"""
''''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
# 利用栈对二叉树进行遍历，用一个额外的数组保存所有二叉树路径的节点和，判断每个保存节点和的数组里有多少个和sum相等的数即可。
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        res = 0
        stack = [(root, [root.val])]
        while stack:
            node, s = stack.pop()
            res += s.count(sum)
            s += [0]

            if node.left:
                stack.append((node.left, [i + node.left.val for i in s]))

            if node.right:
                stack.append((node.right, [i + node.right.val for i in s]))
        return res

