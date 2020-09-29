#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/17 下午6:58
@Author : Catherinexxx
@Site : 
@File : LCOF重建二叉树通过前中还原树.py
@Software: PyCharm
"""
# 通过前序和中序遍历还原二叉树， 用递归 O(n) O(n)
def restruct_tree(pre_order, in_order):
    # 排出两种特殊情况
    if len(pre_order) == 0:
        return 0
    elif len(in_order) == 1:
        return TreeNode(in_order[0])
    else:
        root = pre_order[0]
        depth = in_order.index(root)

        temp = TreeNode(root)
        temp.left = restruct_tree(pre_order[1: depth + 1], in_order[: depth])
        temp.right = restruct_tree(pre_order[depth + 1:], in_order[depth + 1:])
    return temp

# 迭代
