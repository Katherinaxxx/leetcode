#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/16 下午3:59
@Author : Catherinexxx
@Site : 
@File : 13. Roman to Integer.py
@Software: PyCharm
"""
"""
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
"""
# 暴力 有6个小的在左边的例子 超时
class Solution:
    def romanToInt(self, s: str) -> int:
        n, i = len(s), 0
        res = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        while i < n:
            if s[i] == 'I':
                if i + 1 < n and (s[i+1] == 'V' or s[i+1] == 'X'):
                    res += d[s[i+1]] - d[s[i]]
                    i += 2
            elif s[i] == 'X':
                if i + 1 < n and (s[i+1] == 'L' or s[i+1] == 'C'):
                    res += d[s[i+1]] - d[s[i]]
                    i += 2
            elif s[i] == 'C':
                if i + 1 < n and (s[i+1] == 'D' or s[i+1] == 'M'):
                    res += d[s[i+1]] - d[s[i]]
                    i += 2
            else:
                res += d[s[i]]
                i += 1
        return res

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
    # dict.get(key, default=None) 如果key不存在可 返回default

# 首先建立一个HashMap来映射符号和值，然后对字符串从左到右来，如果当前字符代表的值不小于其右边，就加上该值；否则就减去该值。以此类推到最左边的数，最终得到的结果即是答案
# O(n) O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        h = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        ans = 0
        for i in range(len(s)):
            if i<len(s)-1 and h[s[i]] < h[s[i+1]]:
                ans -= h[s[i]]
            else:
                ans += h[s[i]]
        return ans8