#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/14 下午3:53
@Author : Catherinexxx
@Site : 
@File : 725. Split Linked List in Parts.py
@Software: PyCharm
"""
"""
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-linked-list-in-parts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ans, nodes = [], []
        while root:
            nodes.append(root)
            root = root.next
        (p, q), j, n = divmod(len(nodes), k), 0, len(nodes)
        for i in range(k):
            if j < n:
                ans.append(nodes[j])
                j += p + (i < q)
                nodes[j - 1].next = None
            else:
                ans.append(None)
        return ans