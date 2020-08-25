#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/18 下午9:47
@Author : Catherinexxx
@Site : 
@File : 557. Reverse Words in a String III.py
@Software: PyCharm
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''

        sl = s.split()

        def helper(s):
            res = ''
            for i in range(len(s)-1,-1,-1):
                res += s[i]
            return res
        new_sl = list(map(helper, sl))
        return ' '.join(new_sl)

    def reverseWords(self, s):
        return ' '.join(x[::-1] for x in s.split())