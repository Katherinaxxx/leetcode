#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/25 下午10:53
@Author : Catherinexxx
@Site : 
@File : 17.10. Find Majority Element LCCI.py
@Software: PyCharm
"""

# 排序后看中间两个数是否相等
# 时间复杂度O(nlogn)
# 空间复杂度 O(1)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        nums.sort()
        m, n = (len(nums)+1)//2, len(nums)//2
        return nums[m-1] if nums[m-1]==nums[n] else -1