#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/8/3 9:58 PM
@Author : Catherinexxx
@File : 剑指 Offer 52. 两个链表的第一个公共节点.py
@Description: 输入两个链表，找出它们的第一个公共节点。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# hash O(n) O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dic = []
        cur = headA
        while cur:
            dic.append(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in dic: return cur
            cur = cur.next
        return None

# O(n) O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p, q = headA, headB
        while not p == q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

