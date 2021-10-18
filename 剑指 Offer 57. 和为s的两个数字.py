#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/7/29 9:56 PM
@Author : Catherinexxx
@File : 剑指 Offer 57. 和为s的两个数字.py
@Description: 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
"""
# hash O(n) O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for x in nums:
            if x not in dic:
                dic[x] = 0
        for x in nums:
            t = target - x
            if t in dic:
                return [x, t]
        return []

# 双指针 O(n) O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []