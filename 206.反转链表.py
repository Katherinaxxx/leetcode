"""
Date: 2022-12-22 16:21:24
LastEditors: yhxiong
LastEditTime: 2022-12-23 09:48:59
Description: 
"""
#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        a->b->c->d->None
        None<-a<-b c->d
        """
        cur = head
        prev = None
        while cur:
            next = cur.next    
            cur.next = prev
            prev = cur
            cur = next
        return prev
        
        
# @lc code=end

