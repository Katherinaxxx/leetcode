#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/13 下午3:41
@Author : Catherinexxx
@Site : 
@File : 14. Longest Common Prefix.py
@Software: PyCharm
"""
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""

# 水平搜索 O(s) s-所有字符串字符数总和 O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]: return ''
        res = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j<len(strs[i]) and j<len(res) and strs[i][j] == res[j]:
                j += 1
            res = res[:j]
            if not res: return res
        return res
# zip函数 https://www.runoob.com/python/python-func-zip.html
# O(n)time O(1)spqce
class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ''
        for i in zip(*strs):
            # set若不=1说明还有其他元素 则证明元素不一样
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans