#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/26 下午1:38
@Author : Catherinexxx
@Site : 
@File : 面试题 02.01. 移除重复节点.py
@Software: PyCharm
"""
"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# hash判重 O(n)time O(n)space
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        val_set = set()
        prev = ListNode(-1)
        prev.next = head

        while prev.next:
            if prev.next.val in val_set:
                prev.next = prev.next.next
            else:
                val_set.add(prev.next.val)
                prev = prev.next

        return head


