#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/15 下午3:59
@Author : Catherinexxx
@Site : 
@File : 91. 解码方法Decode Ways.py
@Software: PyCharm
"""
# DP O(n) O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if not s or s[0]=="0" :
            return 0
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(1,n):
            if(s[i]=="0"):
                if(s[i-1]=="1" or s[i-1]=="2"):
                    dp[i+1]=dp[i-1]
                else:
                    return 0
            else:
                if(s[i-1]=="1" or (s[i-1]=="2" and "1"<=s[i]<="6")):
                    dp[i+1]=dp[i]+dp[i-1]
                else:
                    dp[i+1]=dp[i]
        return dp[-1]

# dp优化空间 用滚动数组 O(n) O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        a, b = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    a, b = b, a
                else:
                    return 0
            else:
                if s[i-1] == '1' or (s[i-1]=='2' and '0'<=s[i]<='6'):
                    a, b = b, a + b
                else:
                    a, b = b, b
        return b
# 晦涩
class Solution:
    def numDecodings(self, s: str) -> int:
        pp, p = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pp, p = p, pp * (9 < int(s[i-1:i+1]) <= 26) + p * (int(s[i]) > 0)
        return p

