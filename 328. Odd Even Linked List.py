#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/14 下午3:22
@Author : Catherinexxx
@Site : 
@File : 328. Odd Even Linked List.py
@Software: PyCharm
"""
"""
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/odd-even-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 双指针O(n)
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:return head
        odd = head
        even_head = even = head.next
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd,even = odd.next,even.next
        odd.next = even_head
        return head