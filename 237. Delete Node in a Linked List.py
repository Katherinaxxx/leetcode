#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/28 下午12:01
@Author : Catherinexxx
@Site : 
@File : 237. Delete Node in a Linked List.py
@Software: PyCharm
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next