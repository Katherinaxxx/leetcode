#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/8 下午3:22
@Author : Catherinexxx
@Site : 
@File : 647. Palindromic Substrings.py
@Software: PyCharm
"""
"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
"""


# DP O(n^2)time O(n^2)space
# dp[i][j]表示至第i-j个字符是回文子串
# 若第i个字符和前面的不构成回文 cnt += 1
# 若第i个字符和前面的构成回文 cnt += 1 + j 写的不好 意会

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         dp = [[False for _ in range(len(s))] for _ in range(len(s))]
#         cnt = len(s)
#         for r in range(1, len(s)):
#             for l in range(r):
#                 # 如果头尾字符相等and(中间也是回文or头尾之间至多有一个字符）直接返回 True
#                 # 否则要继续看收缩以后的区间的回文性
#                 if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
#                     dp[l][r] = True
#                     cnt += 1
#         return cnt

# 中心扩展 O(n^2)time O(1) time
class Solution:
    def countSubstrings(self, s: str) -> int:
        def get_Center(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count

        n = len(s)
        cnt = 0
        for i in range(len(s)):
            count_even = get_Center(i, i)
            count_odd = get_Center(i, i + 1)
            cnt += count_even + count_odd
        return cnt