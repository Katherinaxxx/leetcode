#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/19 下午2:35
@Author : Catherinexxx
@Site : 
@File : 567. Permutation in String.py
@Software: PyCharm
"""
"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。
"""
# 滑窗法 类似76. Minimum Window Substring
# O(n)time O(n)space
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        target = Counter(s1)
        l, r = 0,0
        lookup = Counter()
        # while r < len(s2):
        for r in range(len(s2)):
            lookup[s2[r]] += 1
            # r += 1
            while all(map(lambda x:lookup[x]>=target[x], target.keys())):
                # if r - l == len(s1):
                if r - l + 1 == len(s1):
                    return True
                lookup[s2[l]] -= 1
                l += 1
        return False