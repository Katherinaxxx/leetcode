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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res