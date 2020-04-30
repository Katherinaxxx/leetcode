#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/30 下午2:36
@Author : Catherinexxx
@Site : 
@File : 581. Shortest Unsorted Continuous Subarray.py
@Software: PyCharm
"""
'''
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。
'''

# 排序后比较下标
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        return len(diff) and max(diff) - min(diff) + 1      # len(diff)数组为空时
