#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/29 下午3:17
@Author : Catherinexxx
@Site : 
@File : 160. Intersection of Two Linked Lists.py
@Software: PyCharm
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 暴力 两层遍历 O(n^2)

# 把一个存到hash表
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = set()
        cur1 = headA
        cur2 = headB
        while cur1:
            A.add(cur1)
            cur1 = cur1.next
        while cur2:
            if cur2 in A:
                return cur2
            cur2 = cur2.next
        return None


# 如果两个链表相交，那么相交点之后的长度是相同的

# 我们需要做的事情是，让两个链表从同距离末尾同等距离的位置开始遍历。这个位置只能是较短链表的头结点位置。
# 为此，我们必须消除两个链表的长度差

# 指针 pA 指向 A 链表，指针 pB 指向 B 链表，依次往后遍历
# 如果 pA 到了末尾，则 pA = headB 继续遍历
# 如果 pB 到了末尾，则 pB = headA 继续遍历
# 比较长的链表指针指向较短链表head时，长度差就消除了
# 如此，只需要将最短链表遍历两次即可找到位置
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        cur2 = headB
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1
