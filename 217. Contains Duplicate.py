#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/27 下午1:54
@Author : Catherinexxx
@Site : 
@File : 217. Contains Duplicate.py
@Software: PyCharm
"""
"""
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
"""
# 排序后 遍历 O(nlogn)time O(1)space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

# hash O(n)time O(n)space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for x in nums:
            if x in s:
                return True
            else:
                s[x] = 1
        return False

# hash O(1)time O(n)space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))