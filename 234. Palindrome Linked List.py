#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/30 下午1:49
@Author : Catherinexxx
@Site : 
@File : 234. Palindrome Linked List.py
@Software: PyCharm
"""
'''
请判断一个链表是否为回文链表。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 两次遍历
# step1 第一次遍历把节点数存入stack step2 第二次遍历pop stack与之比较从而判断是否回文
# time O(n). space O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        cur = head
        # step1
        while cur:
            stack.append(cur.val)
            cur = cur.next
        # step 2
        while head:
            cmp = stack.pop()
            if head.val != cmp:
                return False
            head = head.next
        return True

# 快慢指针+遍历
# step1 快（一次走两步）慢指针找出中间位置 并同时把前面的一半放入stack step2 遍历后半部分与stack pop比较
# time O(n)  space O(n)
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         quick, slow, stack = head, head, []
#         # step1
#         while quick:
#             stack.append(slow.val)
#             slow = slow.next
#             if quick.next:
#                 quick = quick.next.next
#             else:
#                 stack.pop()             # 奇数quick.next为None 且要pop出去一个
#                 break
#         # step2
#         while slow:
#             cmp = stack.pop()
#             if slow.val != cmp:
#                 return False
#             slow = slow.next
#         return True

# 快慢指针+反转+遍历比较+复原
# time O(n) space O(1)
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         slow = head
#         fast = head
#         prev = None
#         flag = True
#         # step1: reverse
#         while(fast and fast.next):
#             fast = fast.next.next
#             temp = slow.next
#             slow.next = prev
#             prev = slow
#             slow = temp
#         # step2: compare
#         if fast: # 奇数
#             node1 = prev
#             node2 = slow.next
#         else: # 偶数
#             node1 = prev
#             node2 = slow
#         while(node1 and node2):
#             if node1.val != node2.val:
#                 flag = False
#             node1, node2 = node1.next, node2.next
#         # step3: recover(optional)
#         back = slow
#         while(prev):
#             temp = prev.next
#             prev.next = back
#             back = prev
#             prev = temp
#         return flag