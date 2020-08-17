#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/22 下午2:20
@Author : Catherinexxx
@Site : 
@File : 297. Serialize and Deserialize Binary Tree.py
@Software: PyCharm
"""
"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"  # 基线条件
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def dfs(alist):
            if alist[0] == "None":
                alist.pop(0)
                return None
            root = TreeNode(alist[0])
            alist.pop(0)
            root.left = dfs(alist)
            root.right = dfs(alist)  # 注意：此处的两个alist,实际大小并不相同
            return root

        if not data:
            return None
        return dfs(data.split(","))


# 用栈遍历 这种的代码更容易理解
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return
        dq = deque([root])
        seq = []
        while dq:
            node = dq.popleft()
            if node is None:
                seq.append('null')
                continue
            seq.append(str(node.val))
            dq.extend([node.left, node.right])
        return ','.join(seq)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        seq = data.split(',')
        root = TreeNode(int(seq[0]))
        dq = deque([root])
        i = 0
        while dq:
            node = dq.popleft()
            i += 1
            if seq[i] != 'null':
                node.left = TreeNode(int(seq[i]))
                dq.append(node.left)
            i += 1
            if seq[i] != 'null':
                node.right = TreeNode(int(seq[i]))
                dq.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))