#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/19 下午1:15
@Author : Catherinexxx
@Site : 
@File : 76. Minimum Window Substring.py
@Software: PyCharm
"""
"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
"""
# 滑动窗口
# 解法1 好想  O(n)time O(n)space
class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import Counter
        t = Counter(t)
        # 窗口内出现的计数
        lookup = Counter()
        start = 0
        end = 0
        min_len = float("inf")
        res = ""
        while end < len(s):
            lookup[s[end]] += 1
            end += 1
            # 当t的每个字符均出现
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                # 若长度减小 则更新结果
                if end - start < min_len:
                    res = s[start:end]
                    min_len = end - start
                # 左边右移
                lookup[s[start]] -= 1
                start += 1
        return res

# # 解法2 但是这个并不好想
# class Solution:
#     def minWindow(self, s: 'str', t: 'str') -> 'str':
#         from collections import defaultdict
#         lookup = defaultdict(int)
#         # lookup是t的字典
#         for c in t:
#             lookup[c] += 1
#         start = 0
#         end = 0
#         min_len = float("inf")
#         counter = len(t)
#         res = ""
#         while end < len(s):
#             # 若右边在t中
#             if lookup[s[end]] > 0:
#                 counter -= 1
#             # 滑动过程中的词都在字典中减少
#             lookup[s[end]] -= 1
#             end += 1
#             # 当t中单词都出现过 下面优化找到最短 左边右滑
#             while counter == 0:
#                 if min_len > end - start:
#                     min_len = end - start
#                     res = s[start:end]
#                 # 如果左边的词没有在t中 or 出现过次数正好抵消
#                 if lookup[s[start]] == 0:
#                     counter += 1
#                 lookup[s[start]] += 1
#                 start += 1
#         return res