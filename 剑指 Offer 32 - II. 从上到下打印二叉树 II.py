'''
Author: Catherine Xiong
Date: 2021-07-26 22:45:31
LastEditTime: 2021-09-28 00:04:20
LastEditors: Catherine Xiong
Description: 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(n) time O(n) space
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur_res = []
            for _ in range(len(queue)):
                cur = queue.popleft()   # 双端队列O(1) list O(n)
                cur_res.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            res.append(cur_res)
        return res

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        cur_level = [root]
        while cur_level:
            next_level = []
            for node in cur_level:
                res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
        return res



