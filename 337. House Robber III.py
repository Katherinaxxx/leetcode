#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/12 下午5:46
@Author : Catherinexxx
@Site : 
@File : 337. House Robber III.py
@Software: PyCharm
"""
"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归DP [根+左右不选的最大，左右（选不选）的最大]
class Solution:

    def dp(self, cur: TreeNode) -> List[int]:
        if not cur:
            return [0, 0]

        l = self.dp(cur.left)
        r = self.dp(cur.right)

        return [max(l) + max(r), cur.val + l[0] + r[0]]

    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))