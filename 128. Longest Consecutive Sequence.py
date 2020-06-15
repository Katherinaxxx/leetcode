#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/22 下午1:25
@Author : Catherinexxx
@Site : 
@File : 128. Longest Consecutive Sequence.py
@Software: PyCharm
"""
"""
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。
"""
# 1. 暴力 枚举每个数为起始点 O(n) * while next存在 O(n) * 继续往下找O(n)=O(n^3)time
# 2. 先排序 再找 O(nlogn)
# class Solution:
#     def longestConsecutive(self, nums):
#         if not nums:
#             return 0

#         nums.sort()

#         longest_streak = 1
#         current_streak = 1

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i-1]:
#                 if nums[i] == nums[i-1]+1:
#                     current_streak += 1
#                 else:
#                     longest_streak = max(longest_streak, current_streak)
#                     current_streak = 1

#         return max(longest_streak, current_streak)

# 3. hashset O(n)time题解这么写但我还是觉得有点牵强
class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        length, res = 1, 0
        for i in  s:
            # 若当前点是起点
            if i-1 not in s:
                length = 1
                cur = i
                while cur+1 in s:
                    length += 1
                    cur += 1
                res = max(length, res)
        return res