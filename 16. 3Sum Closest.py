#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/18 下午10:13
@Author : Catherinexxx
@Site : 
@File : 16. 3Sum Closest.py
@Software: PyCharm
"""
# 排序 遍历 + 双指针 O(nlogn)+O(n^2)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")
        for ix,x in enumerate(nums):
            t = target - x
            i, j = ix+1, len(nums)-1
            while i <j:
                if nums[i] + nums[j] == t:
                    return target
                elif abs(x+nums[i]+nums[j]-target) < abs(res-target):
                    res = x + nums[i] + nums[j]
                elif nums[i] + nums[j] < t:
                    i += 1
                else:
                    j -= 1
        return res
