#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/16 下午3:48
@Author : Catherinexxx
@Site : 
@File : 3. Longest Substring Without Repeating Characters.py
@Software: PyCharm
"""
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""


# 滑动窗口模版 time O(n^2) space O(1)
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            # 之前走过
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            # 当前有重复的 左窗口缩小
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len

# 重复下标 本题最优 time O(n) space O(n)
# hash存字母下标 出现重复字符则更新起始位置 否则hash增加元素且更新长度
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, res, lookup = -1, 0, {}
        for idx, val in enumerate(s):
            if val in lookup and lookup[val] > start:
                start = lookup[val]
                lookup[val] = idx
            else:
                lookup[val] = idx
                res = max(res, idx - start)
        return res