#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/23 下午6:54
@Author : Catherinexxx
@Site : 
@File : 92.Reverse Linked List II.py
@Software: PyCharm
"""

# 分成三段，前，中反转（递归），后 再连起来

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        a, d = dummy, dummy
        for _ in range(m - 1):
            a = a.next
        for _ in range(n):
            d = d.next
        # a为m前 d为n前
        b, c = a.next, d.next
        # b为中间需要反转的 c为后面的
        pre = b
        cur = pre.next
        while cur != c:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        a.next = d
        b.next = c
        return dummy.next
