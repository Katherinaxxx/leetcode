#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/17 上午11:44
@Author : Catherinexxx
@Site : 
@File : 206. Reverse Linked List.py
@Software: PyCharm
"""
# 迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        start = ListNode(0)
        while head:
            tmp = ListNode(head.val)
            tmp.next = start.next
            start.next = tmp
            head = head.next
        return start.next

## 递归
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         start = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return start
