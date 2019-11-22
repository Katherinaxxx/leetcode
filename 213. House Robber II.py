#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/15 下午12:31
@Author : Catherinexxx
@Site : 
@File : 213. House Robber II.py
@Software: PyCharm
"""
# 两DP 头要尾不要 尾要头不要
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(n):
            last, now = 0, 0
            for i in n: last, now = now, max(last + i, now)
            return now
        return max(helper(nums[1:len(nums)]), helper(nums[0:len(nums)-1]))