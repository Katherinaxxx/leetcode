#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/15 下午2:11
@Author : Catherinexxx
@Site : 
@File : 395. Longest Substring with At Least K Repeating Characters.py
@Software: PyCharm
"""
"""
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
"""
#   分治 低频字符切分 O(nlogn)应该
class Solution(object):
    def longestSubstring(self, s, k):
        if not s:
            return 0
        for c in set(s):
            # 满足分割条件，进行分割
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        # 如果每个字符出现的次数均不小于k，则返回当前字符串的长度
        return len(s)