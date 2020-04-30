#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/23 下午10:08
@Author : Catherinexxx
@Site : 
@File : Add Two Numbers.py
@Software: PyCharm
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        node = res
        tmp = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + tmp
            tmp = s // 10
            node.next = ListNode(s % 10)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            node = node.next

        if tmp == 1:  # 判断最后一位是否需要进位
            node.next = ListNode(1)

        return res.next