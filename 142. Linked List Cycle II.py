#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/16 上午11:42
@Author : Catherinexxx
@Site : 
@File : 142. Linked List Cycle II.py
@Software: PyCharm
"""
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 
如果 pos 是 -1，则在该链表中没有环。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 遍历+hashmap 直观好想
# O(n)time O(n)space
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = {}
        # visited = set()
        node = head
        while node:
            if node not in visited:
                visited[node] = 1
                # visited.add(node)
                node = node.next
            else:
                return node
        return None


快慢指针 Floyd解法 step1重合就有环 step2重合点、起始点开始跑 重合点为环起始点
O(n) time O(1)space

class Solution(object):
    def getIntersect(self, head):
        tortoise = head     # 慢
        hare = head         # 快

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise

        return None

    def detectCycle(self, head):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an e***ance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the e***ance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1