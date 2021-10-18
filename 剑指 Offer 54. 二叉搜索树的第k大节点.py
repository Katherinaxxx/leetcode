'''
Author: Catherine Xiong
Date: 2021-09-09 19:34:37
LastEditTime: 2021-09-09 19:36:45
LastEditors: Catherine Xiong
Description: 给定一棵二叉搜索树，请找出其中第k大的节点。
'''
# 中序遍历，返回遍历结果的倒数第k个
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res[-k]