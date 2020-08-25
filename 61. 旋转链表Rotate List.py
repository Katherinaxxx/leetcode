#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/24 下午8:27
@Author : Catherinexxx
@Site : 
@File : 61. 旋转链表Rotate List.py
@Software: PyCharm
"""

# time O(n) space O(1)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None: return head
        # 计算长度
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        if k % length == 0:  # 若不移动直接返回
            return head

        # 取出旋转链表
        length -= k % length
        cur = head
        while length > 1:
            cur = cur.next
            length -= 1
        tmp = cur.next
        cur.next = None  # head去尾

        # 移动到链表尾部
        cur1 = tmp
        while cur1 and cur1.next:
            cur1 = cur1.next
        cur1.next = head

        return tmp


