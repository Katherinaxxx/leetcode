#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/16 下午3:21
@Author : Catherinexxx
@Site : 
@File : 139. Word Break.py
@Software: PyCharm
"""
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
"""

# DP dp[i]表示前i个是否可以用wordDict表示 return dp[-1]
# O(n^2)time O(n)space
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)      # True:空字符自然是没问题的
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]