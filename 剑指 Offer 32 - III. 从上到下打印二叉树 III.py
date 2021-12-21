'''
Author: Catherine Xiong
Date: 2021-12-14 19:01:11
LastEditTime: 2021-12-14 19:23:11
LastEditors: Catherine Xiong
Description: 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        s, next_ = [root], []
        res, res_ = [], []
        flag = 1
        while s:
            cur = s.pop()
            if cur:
                res_.append(cur.val) 
                if flag == -1:
                    next_.append(cur.right)
                    next_.append(cur.left)
                else:
                    next_.append(cur.left)
                    next_.append(cur.right)
            if not s and res_:
                s = next_
                res.append(res_)
                flag *= -1
                next_, res_ = [], []
        return res


import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: tmp.appendleft(node.val) # 偶数层 -> 队列头部
                else: tmp.append(node.val) # 奇数层 -> 队列尾部
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))
        return res

