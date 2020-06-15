#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/19 下午2:19
@Author : Catherinexxx
@Site : 
@File : 209. Minimum Size Subarray Sum.py
@Software: PyCharm
"""
"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 滑窗法 O(n)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r, _s = 0, 0, 0
        length = float("inf")

        # while r < len(nums):
        for r in range(len(nums)):
            _s += nums[r]
            # r += 1
            # 和满足要求 则接着找最短
            while _s >= s:
                # length = min(length, r-l)
                length = min(length, r - l + 1)
                _s -= nums[l]
                l += 1

        return length if length != float("inf") else 0