#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/12 下午5:51
@Author : Catherinexxx
@Site : 
@File : LCOF38. 字符串的排列.py
@Software: PyCharm
"""

# 递归 O(n!) O(n^2)
class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + nums[i])
        backtrack(s, '')
        return list(set(res))

# 不用set去重
class Solution:
    def permutation(self, s: str) -> List[str]:
        #思路：dfs同时记录路径，到根节点处统计结果
        s = sorted(list(s))

        res = []
        def dfs(s,road):
            if s == []:
                res.append(road)
            for i in range(len(s)):
                # 去重
                if i>0 and s[i] == s[i-1]:continue
                dfs(s[:i]+s[i+1:], road+s[i])
        dfs(s,'')
        return res