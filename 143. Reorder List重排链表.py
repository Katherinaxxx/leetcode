#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/10/20 下午8:45
@Author : Catherinexxx
@Site : 
@File : 143. Reorder List重排链表.py
@Software: PyCharm
"""
"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        def findMid(node):
            slow = fast = node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(node):
            pre, cur = None, node
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
            return pre

        def merge(node1, node2):
            while node1 and node2:
                node1.next, node2.next, node1, node2 = node2, node1.next, node1.next, node2.next

        mid = findMid(head)
        l1, l2 = head, mid.next
        # break the list or there will be cycle
        mid.next = None
        l2 = reverse(l2)
        merge(l1, l2)