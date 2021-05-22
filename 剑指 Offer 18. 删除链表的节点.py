#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/4/21 8:28 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 剑指 Offer 18. 删除链表的节点.py
@Description: 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# O(n)time O(1)space
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        if head.val == val: return head.next
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            head = head.next
        return res.next

# 双指针 O(n)time O(1)space 更简洁
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur.val != val:
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return dummy.next


# 递归
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        if head.val == val:
            return head.next
        head.next = self.deleteNode(head.next, val)
        return head



