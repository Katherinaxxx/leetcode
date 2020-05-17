#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/16 下午2:51
@Author : Catherinexxx
@Site : 
@File : 560. Subarray Sum Equals K.py
@Software: PyCharm
"""
"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
"""
# 前序和 hashmap
# o(n)time O(n)space
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        acc = count = 0
        for num in nums:
            acc += num
            # 显然 若当前和=k cnt+1
            if acc == k:
                count += 1
            # 若 当前和-k 已然出现过 说明某一部分子序列的和=k cnt+ （当前和-k）出现的次数
            if acc - k in d:
                count += d[acc-k]
            if acc in d:
                d[acc] += 1
            else:
                d[acc] = 1
        return count
