'''
Author: Catherine Xiong
Date: 2021-12-02 20:02:29
LastEditTime: 2021-12-02 20:02:29
LastEditors: Catherine Xiong
Description: 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.res = []
        def recursion(root, path, target):
            if not root:
                return 
            path.append(root.val)
            if not root.left and not root.right and sum(path)==target:
                self.res.append(path)
                return 
            recursion(root.left, path[:], target)
            recursion(root.right, path[:], target)
        recursion(root, [], target)
        return self.res