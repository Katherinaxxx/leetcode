#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/10 下午2:47
@Author : Catherinexxx
@Site : 
@File : 131. Palindrome Partitioning.py
@Software: PyCharm
"""
"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。
"""
# 递归 前部分是回文 后半部分继续
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])
        helper(s, [])
        return res

# 递归2
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(1, len(s)+1):
            if s[:i][::-1] == s[:i]:
                res += [[s[:i]]+j for j in self.partition(s[i:])]
        return res

