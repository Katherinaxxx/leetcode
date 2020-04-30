#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/28 下午1:50
@Author : Catherinexxx
@Site : 
@File : 136. Single Number.py
@Software: PyCharm
"""

# 1 暴力遍历两次 O(n^2)
# 2 排序 时O(nlogn) 空O(n) 不满足要求
# 3 异或 中间重复的会抵消  O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res