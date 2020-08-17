#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/12/10 下午12:07
@Author : Catherinexxx
@Site : 
@File : 5. Longest Palindromic Substring.py
@Software: PyCharm
"""


# 暴力 O(n^3)
# 1、 枚举中心（可以使元素odd或者两个元素中间即无元素even） 向两边扩展 O(n^2)
# 写法1
# class Solution:
#     def __init__(self):
#         self.lo = 0
#         self.maxlen = 0
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2: return s
#         for i in range(len(s)):
#             self.extend_palindrome(s, i, i)          # even
#             self.extend_palindrome(s, i, i+1)        # odd
#         return s[self.lo: self.lo+self.maxlen]
#     def extend_palindrome(self, s, j, k):
#         while j >= 0 and k < len(s) and s[j] == s[k]:
#             j -= 1; k += 1

#         if self.maxlen < k-j-1:
#             self.lo = j+1
#             self.maxlen = k-j-1
# 写法2
class Solution(object):
    def longestPalindrome(self, s):
        len_s = len(s)

        def expand(L, R):
            while L >= 0 and R < len_s and s[L] == s[R]:
                L -= 1
                R += 1
            return L + 1, R - (L + 1)

        l, length = 0, 0
        for i in range(len_s):
            l, length = max((l, length), expand(i, i), expand(i, i + 1), key=lambda t: t[1])
            # t:t[]字母可以随意修改，求最大值方式按照中括号[]里面的维度，[0]按照第一维，[1]按照第二维。
        return s[l: l + length]

# 2、 DP O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
        return res