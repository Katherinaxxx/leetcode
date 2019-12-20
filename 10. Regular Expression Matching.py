#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/12/10 下午3:10
@Author : Catherinexxx
@Site : 
@File : 10. Regular Expression Matching.py
@Software: PyCharm
"""

class Solution(object):

    # 带备忘录的递归
    def isMatch(self, text, pattern):
        memo = dict() # 备忘录
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(pattern): return i == len(text)

            first = i < len(text) and pattern[j] in {text[i], '.'}

            if j <= len(pattern) - 2 and pattern[j + 1] == '*':
                ans = dp(i, j + 2) or \
                        first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

    # 暴力递归
    def isMatch(self, text, pattern):
        if not pattern: return not text

        first = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return self.isMatch(text, pattern[2:]) or \
                    first and self.isMatch(text[1:], pattern)
        else:
            return first and self.isMatch(text[1:], pattern[1:])