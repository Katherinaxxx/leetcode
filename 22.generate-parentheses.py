#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/24 下午6:57
@Author : Catherinexxx
@Site : 
@File : 22.generate-parentheses.py
@Software: PyCharm
"""

# 1、递归所有可能组合 再加条件筛选即可递归出合法组合
class Solution:
    def generateParenthesis(self, n):
        res = []
        def generate(left, right, s):
            if len(s)==2*n:
                res.append(s)
                return
            if left < n:
                generate(left+1, right, s+"(")
            if right < left:
                generate(left, right+1, s+")")
        generate(0, 0, "")
        return res

print(Solution().generateParenthesis(3))