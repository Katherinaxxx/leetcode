#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/24 下午8:04
@Author : Catherinexxx
@Site : 
@File : LCOF03. 数组中重复的数字.py
@Software: PyCharm
"""
# 1 只是时间优先就用字典， O(n)time O(n)space
# 2 还有空间要求，就用指针+原地排序数组， O(nlogn)time O(1)space
# 3 如果面试官要求空间O(1)并且不能修改原数组，还得写成二分法！！！ O(n) O(1)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            if x in d:
                return x
            d[x] = 1
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == nums[i]:
                return pre
            pre = nums[i]
    def findRepeatNumber(self, nums: List[int]) -> int:
        """
        题目中给的元素是 < len（nums）的，所以我们可以让 位置i 的地方放元素i。如果位置i的元素不是i的话，那么我们就把i元素的位置放到它应该在的位置，即 nums[i] 和nums[nums[i]]的元素交换，这样就把原来在nums[i]的元素正确归位了。如果发现 要把 nums[i]正确归位的时候，发现nums[i]（这个nums[i]是下标）那个位置上的元素和要归位的元素已经一样了，说明就重复了，重复了就return
        """
        n = len(nums)
        for i in range(n):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]