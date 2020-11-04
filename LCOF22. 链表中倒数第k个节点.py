#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/10/20 下午8:54
@Author : Catherinexxx
@Site : 
@File : LCOF22. 链表中倒数第k个节点.py
@Software: PyCharm
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 走一遍 数节点数目 再走一遍即可 O(n)time O(1)space
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        nums = 0
        cur = head
        while cur:
            cur = cur.next
            nums += 1
        for i in range(nums-k):
            head = head.next
        return head