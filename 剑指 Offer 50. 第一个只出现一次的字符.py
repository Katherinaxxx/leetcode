#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/7/27 9:28 PM
@Author : Catherinexxx
@File : 剑指 Offer 50. 第一个只出现一次的字符.py
@Description: 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic   # not有点精髓 未出现或者出现过多次都是False
        for c in s:
            if dic[c]: return c
        return ' '

