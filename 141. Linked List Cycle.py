#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/17 上午11:45
@Author : Catherinexxx
@Site : 
@File : 141. Linked List Cycle.py
@Software: PyCharm
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1、暴力：遍历链表 并存入hashmap 若在hashmap中找到 说明有环
# public boolean hasCycle(ListNode head) {
#     Set<ListNode> nodesSeen = new HashSet<>();
#     while (head != null) {
#         if (nodesSeen.contains(head)) {
#             return true;
#         } else {
#             nodesSeen.add(head);
#         }
#         head = head.next;
#     }
#     return false;
# }

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         p = head
#         st = set()
#         while p:
#             if p in st:
#                 return True
#             st.add(p)
#             p = p.next
#         return False
# # 2、快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

# public boolean hasCycle(ListNode head) {
#     if (head == null || head.next == null) {
#         return false;
#     }
#     ListNode slow = head;
#     ListNode fast = head.next;
#     while (slow != fast) {
#         if (fast == null || fast.next == null) {
#             return false;
#         }
#         slow = slow.next;
#         fast = fast.next.next;
#     }
#     return true;
# }