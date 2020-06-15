#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/23 下午7:22
@Author : Catherinexxx
@Site : 
@File : 32. Longest Valid Parentheses.py
@Software: PyCharm
"""
"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。


"""

# 栈 （括号匹配都用栈）
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i - stack[-1])
        return res

# # DP dp[i]表示至i包含有效括号的子串的长度
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         if n == 0: return 0
#         dp = [0] * n
#         res = 0
#         for i in range(n):
#             if i>0 and s[i] == ")":
#                 if  s[i - 1] == "(":
#                     dp[i] = dp[i - 2] + 2
#                 elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
#                     dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
#                 if dp[i] > res:
#                     res = dp[i]
#         return res