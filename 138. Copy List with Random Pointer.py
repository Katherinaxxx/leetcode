#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/2 下午12:33
@Author : Catherinexxx
@Site : 
@File : 138. Copy List with Random Pointer.py
@Software: PyCharm
"""
"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 


"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# DFS
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        lookup = {}

        def dfs(head):
            if not head: return None
            if head in lookup: return lookup[head]
            clone = Node(head.val, None, None)
            lookup[head] = clone
            clone.next, clone.random = dfs(head.next), dfs(head.random)
            return clone

        return dfs(head)


# 一遍节点 一遍random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        lookup = {}
        node = head
        # 创建所有节点
        while node:
            lookup[node] = Node(node.val, None, None)
            node = node.next

        node = head
        # 节点连接
        while node:
            lookup[node].next = lookup.get(node.next)
            lookup[node].random = lookup.get(node.random)
            node = node.next
        return lookup[head]