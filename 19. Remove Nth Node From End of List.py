#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/20 下午6:37
@Author : Catherinexxx
@Site : 
@File : 19. Remove Nth Node From End of List.py
@Software: PyCharm
"""
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 先走一遍 看有多少个节点m 再走第二遍m-n O(m(m-n))time 超时 写的确实太恶心
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         m = 0
#         node = head
#         while node:
#             m += 1
#             node = node.next
#         node = head
#         # 走到倒数第n个的前一个节点pre
#         for _ in range(m-n-1):
#             pre = node.next
#             node = node.next
#         # 总共3个节点及以上
#         if head.next and head.next.next:
#             n_next = head.next.next
#             pre.next = n_next
#         # 总共两个节点
#         elif head.next:
#             if n == 2:
#                 return head.next
#             else:
#                 head.next = None
#                 return head
#         else:
#             return []
#         return head

# 别人写的 思路跟上面是一样的
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         node_no = 0
#         node = head
#         while node is not None:
#             node = node.next
#             node_no += 1
#         # 找到了删除节点的位置
#         node_no -= n + 1

#         node = head
#         if node_no == -1:
#             head = head.next
#         else:
#             while(node_no):
#                 node = node.next
#                 node_no -= 1
#             node.next = node.next.next
#         return head

# 递归 牛逼 可惜我勉强能看懂些自己还是写不出来
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         global i
#         if head is None:
#             i=0
#             return None
#         # 不断把最后next=None i为次数
#         head.next = self.removeNthFromEnd(head.next,n)
#         i+=1
#         return head.next if i==n else head

# 双指针 前面的走到头时 后面的正好走到要删除的位置 O(n)time
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Node = ListNode(None)
        Node.next = head
        first,slow = Node,Node
        for i in range(n):
            first = first.next
        while first.next != None:
            first = first.next
            slow = slow.next
        slow.next = slow.next.next
        return Node.next