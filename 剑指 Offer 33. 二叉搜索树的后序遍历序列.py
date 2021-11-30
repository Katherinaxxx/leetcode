'''
Author: Catherine Xiong
Date: 2021-11-30 20:05:38
LastEditTime: 2021-11-30 20:05:39
LastEditors: Catherine Xiong
Description: 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
'''
"""
 1. 递归 
 最后一个为根节点，从左往右第一个大于根节点的认为是右子树，继续走，若左右子树都是二叉树，则说明是二叉树
 递归判断
"""
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder: return True
        root = postorder[-1]
        cur_index = 0
        while postorder[cur_index] < root:
                cur_index += 1 
        left = postorder[:cur_index]
        right = postorder[cur_index : -1]
        for val in right:
            if val < root:
                return False
        return self.verifyPostorder(left) and self.verifyPostorder(right)
