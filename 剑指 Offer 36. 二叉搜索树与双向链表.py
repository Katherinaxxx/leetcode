'''
Author: Catherine Xiong
Date: 2021-11-16 22:31:21
LastEditTime: 2021-11-16 22:31:21
LastEditors: Catherine Xiong
Description: 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return
        path = []
        def inorder(root):
            if not root: return 
            inorder(root.left)
            path.append(root)
            inorder(root.right)
        # 中序遍历排序    
        inorder(root)
        for i in range(len(path)):
            path[i].left = path[i-1]
            path[i].right = path[(i+1)%len(path)]
        return path[0]