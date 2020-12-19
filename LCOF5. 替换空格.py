#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/7 1:23 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : LCOF5. 替换空格.py
@Description: 
"""
"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""
# O(n)time O(n)space
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            if i == ' ':
                res +=  '%20'
            else:
                res += i
        return res
    def replaceSpace(self, s):
        return ''.join([x if x != ' ' else '%20'for x in s])