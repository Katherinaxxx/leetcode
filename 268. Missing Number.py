#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/21 下午10:53
@Author : Catherinexxx
@Site : 
@File : 268. Missing Number.py
@Software: PyCharm
"""
"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
"""
# 排序
# math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)+1)*len(nums) // 2 - sum(nums)
# 位运算 一个数a对另一个数b做两次抑或运算结果还是b --- a^b^b =a
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing