#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/8/5 11:12 PM
@Author : Catherinexxx
@File : 剑指 Offer 53 - I. 在排序数组中查找数字 I.py
@Description: 统计一个数字在排序数组中出现的次数。
"""


# 遍历 O(n) O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        for x in nums:
            if x == target:
                res += 1
        return res


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = self.binary_search_left(nums, target + 1)
        l = self.binary_search_right(nums, target - 1)
        return r - l

    def binary_search_left(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def binary_search_right(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

