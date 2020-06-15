#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/25 下午12:16
@Author : Catherinexxx
@Site : 
@File : 303. Range Sum Query - Immutable.py
@Software: PyCharm
"""
"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
"""

# 前缀和 O(n)time O(2n)space
class NumArray:

    def __init__(self, nums: List[int]):
        self.part_sum = [[0, 0] for _ in range(len(nums)+2)]
        self.s = sum(nums)
        for i in range(1, len(nums)+1):
            self.part_sum[i][0] = nums[i-1] + self.part_sum[i-1][0]
            self.part_sum[len(nums)+1-i][1] = nums[len(nums)-i] + self.part_sum[len(nums)+2-i][1]
    # 这样减有点复杂 可以优化
    def sumRange(self, i: int, j: int) -> int:
        return self.s - self.part_sum[j+2][1] - self.part_sum[i][0]

# 上面优化的做法 O(n)time O(n)space
class NumArray:
    def __init__(self, nums: List[int]):
        self.part_sum = [0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            self.part_sum[i] = nums[i-1] + self.part_sum[i-1]
    # 这样减有点复杂 可以优化
    def sumRange(self, i: int, j: int) -> int:
        return self.part_sum[j+1] - self.part_sum[i]