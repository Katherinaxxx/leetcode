#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/8 3:59 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : LCOF6. 从尾到头打印链表.py
@Description: 
"""
"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        return self.reversePrint(head.next) + [head.val]