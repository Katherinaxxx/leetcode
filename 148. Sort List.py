#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/8 上午11:24
@Author : Catherinexxx
@Site : 
@File : 148. Sort List.py
@Software: PyCharm
"""
"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 归并排序：快慢指针找到中点 切段 然后merge

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # termination.

        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.

        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)

        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next
