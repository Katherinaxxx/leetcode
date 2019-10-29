#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/25 下午3:44
@Author : Catherinexxx
@Site : 
@File : 17.letter-combinations-of-a-phone-number.py
@Software: PyCharm
"""


# 回溯 O(3^N * 4^M)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
        res = []
        if digits == "":
            return res

        def recursion(next, s):
            if len(next) == 0:
                res.append(s)
                return
            for char in dict.get(next[0]):
                recursion(next[1:], s + char)

        recursion(digits, "")
        return res


# 短 O(n * 3^N * 4^M)
class Solution:
    def letterCombinations(self, digits):
        dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                '8': "tuv", '9': "wxyz"}
        cmb = [''] if digits else []

        for d in digits:
            cmb = [p + q for p in cmb for q in dict[d]]
        return cmb