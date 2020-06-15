#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/26 下午2:38
@Author : Catherinexxx
@Site : 
@File : 23. Merge k Sorted Lists.py
@Software: PyCharm
"""
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 优先队列 O(nlogk)time
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 优先队列
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        # 把所有链表的头节点加入优先队列
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            # 把最小的pop出加到p中
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            # 把pop出得节点所在的链表的头继续加入优先队列
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

# 分治
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2