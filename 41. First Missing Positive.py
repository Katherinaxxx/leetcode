#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/26 下午1:08
@Author : Catherinexxx
@Site : 
@File : 41. First Missing Positive.py
@Software: PyCharm
"""

# 1直观 hash O(n)time O(n)space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or max(nums)<=0:
            return 1
        m = max(nums)
        # 查询更快
        s = set(nums)
        for i in range(1, m+1):
            if i not in s:
                return i
        return m+1

# 2排序后找 O(nlogn)time O(1)space 代码略

# 3将数组视为hash 每个元素x应该位于x-1的位置 之后位置不正确的就是缺失的 若位置都正确则是max+1
# O(n)time. O(1)space
from typing import List


class Solution:

    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方

    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1)

        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1

    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]