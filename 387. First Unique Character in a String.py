#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/16 上午6:20
@Author : Catherinexxx
@Site : 
@File : 387. First Unique Character in a String.py
@Software: PyCharm
"""
"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""
# hash存 查找 O(n)time O(n)space
class Solution(object):

    def firstUniqChar(self, s: str) -> int:
        dic = {}

        # 记录字符出现次数
        for c in s:
            dic[c] = dic[c] + 1 if c in dic else 1

        # 过滤出现次数不为一的字符
        unique_chars = [k for k, v in filter(lambda kvp: kvp[1] == 1, dic.items())]
        # 遍历目标字符串，返回首个出现在unique_chars中的字符的索引
        for i, c in enumerate(s):
            if c in unique_chars:
                return i

        return -1


# counter O(n)time O(n)space
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=Counter(s)
        res=[s.index(i) for i in d if d[i]==1]
        return min(res) if res else -1

# find rfind O(n)time O(1)space
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for c in s:
            if s.find(c) == s.rfind(c):
                return s.find(c)
        return -1