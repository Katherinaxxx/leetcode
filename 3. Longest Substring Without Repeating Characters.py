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

# 重复下标 本题最优
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            # 重复字符出现了
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res

# 滑动窗口模版
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
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len