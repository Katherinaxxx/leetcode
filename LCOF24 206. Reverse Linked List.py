#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/17 上午11:44
@Author : Catherinexxx
@Site : 
@File : LCOF24 206. Reverse Linked List.py
@Software: PyCharm
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 迭代 O(n) O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nexttmp = cur.next
            cur.next = pre
            pre = cur
            cur = nexttmp
        return pre


'''
在思考递归问题的时候，我们要从上到下思考：
子问题是什么
base case是什么
在当前层要干什么
对翻转链表来说，以1->2->3->4->5为例：
子问题是：除去current node，翻转剩余链表，即除去1, reverseList(2->3->4->5),递归得到的解是 5->4->3->2
base case:当前节点为空，返回空，当前节点的next为空（只剩余一个节点），返回该节点
在当前层要干什么：翻转链表，即把1->2变为2->1.
最后return的是结果链表的头，也就是递归解的头。

'''

# 递归 O(n) O(n)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 把next反转 并指向head
        start = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return start

