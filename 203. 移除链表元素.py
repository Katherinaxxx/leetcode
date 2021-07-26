#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/6/5 10:38 AM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 203. 移除链表元素.py
@Description: 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 递归
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
        # 迭代


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if not head:
            return head
        dummy = ListNode(0, head)
        temp = dummy
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next

