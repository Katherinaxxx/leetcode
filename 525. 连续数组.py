#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/6/3 12:24 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 525. 连续数组.py
@Description: 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
"""
# 把0换成-1 前缀和
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        presum, res = 0, 0
        h = {0:-1}
        for i, x in enumerate(nums):
            presum += x
            if presum in h:
                res = max(res, i-h[presum])
            else:
                h[presum] = i
        return res

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        presum, res = 0, 0
        h = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
            presum += nums[i]
            if presum in h:
                res = max(res, i-h[presum])
            else:
                h[presum] = i
        return res

